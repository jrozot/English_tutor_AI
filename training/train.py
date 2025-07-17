import os
import json
import torch
import logging
from datasets import load_dataset, DatasetDict
from transformers import (
    AutoTokenizer,
    EncoderDecoderModel,
    DataCollatorForSeq2Seq,
    Seq2SeqTrainer,
    Seq2SeqTrainingArguments,
    EarlyStoppingCallback
)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load model config
CONFIG_PATH = os.path.join("models", "model_config.json")
with open(CONFIG_PATH, "r") as f:
    config = json.load(f)

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained("t5-small")  # Or any other Transformer-based model

# Load dataset (replace with actual cleaned CSV)
logger.info("Loading dataset...")
try:
    dataset = load_dataset("csv", data_files={
        "train": "data/train_cleaned.csv",
        "validation": "data/validation_cleaned.csv"
    })
except Exception as e:
    logger.error("Dataset not found. Ensure CSVs are in `data/`. Error: %s", e)
    exit(1)

# Preprocessing function
def preprocess(example):
    source = example["incorrect"]
    target = example["correct"]

    inputs = tokenizer(source, truncation=True, padding="max_length",
                       max_length=config["training"]["max_seq_length"])
    targets = tokenizer(target, truncation=True, padding="max_length",
                        max_length=config["training"]["max_seq_length"])

    inputs["labels"] = targets["input_ids"]
    return inputs

logger.info("Tokenizing dataset...")
tokenized = dataset.map(preprocess, batched=True, remove_columns=["incorrect", "correct"])

# Define model
logger.info("Loading model...")
model = EncoderDecoderModel.from_encoder_decoder_pretrained("t5-small", "t5-small")

# Training arguments
training_args = Seq2SeqTrainingArguments(
    output_dir="./models/grammar_corrector_output",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=config["training"]["learning_rate"],
    per_device_train_batch_size=config["training"]["batch_size"],
    per_device_eval_batch_size=config["training"]["batch_size"],
    weight_decay=config["training"]["weight_decay"],
    save_total_limit=2,
    num_train_epochs=config["training"]["num_epochs"],
    predict_with_generate=True,
    fp16=torch.cuda.is_available(),
    logging_dir="./logs",
    logging_steps=50,
    load_best_model_at_end=True,
    metric_for_best_model="loss",
    report_to="none"
)

# Data collator for dynamic padding
data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

# Trainer
trainer = Seq2SeqTrainer(
    model=model,
    args=training_args,
    train_dataset=tokenized["train"],
    eval_dataset=tokenized["validation"],
    tokenizer=tokenizer,
    data_collator=data_collator,
    callbacks=[EarlyStoppingCallback(early_stopping_patience=2)]
)

# Train
logger.info("Starting training...")
trainer.train()

# Save final model
logger.info("Saving final model and tokenizer...")
model.save_pretrained("./models/final_grammar_model")
tokenizer.save_pretrained("./models/final_grammar_model")

logger.info("Training complete.")
