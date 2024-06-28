python train_model.py --train PATH_TO_TRAIN \
                    --dev PATH_TO_DEV \
                    --out_dir training \
                    --model_name MODEL_NAME \
                    --gpus 1 \
                    --epochs 50 \
                    --encoder_model xlm-roberta-base \
                    --batch_size 64 \
                    --lr 0.00002

# PATH_TO_TRAIN replace with its own path like: "/path/to/data/multiconer2022/RU-Russian/ru_train.conll"
# PATH_TO_DEV replace with its own path like: "/path/to/data/multiconer2022/RU-Russian/ru_dev.conll"
# MODEL_NAME replace with your model name, like: "xlmr_ner_ru"