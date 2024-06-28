python evaluate.py --test PATH_TO_TEST \
                --out_dir validation \
                --gpus 1 \
                --encoder_model xlm-roberta-base \
                --model PATH_TO_MODEL \
                --prefix MODEL_NAME

# PATH_TO_TEST replace with its own path like: "/path/to/data/multiconer2022/RU-Russian/ru_test.conll"
# PATH_TO_MODEL replace with its own path like: "./xlmr_ner_ru/lightning_logs/version_3538632"
# MODEL_NAME replace with your model name, like: "xlmr_ner_ru"