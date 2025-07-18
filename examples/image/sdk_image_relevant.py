from dingo.exec import Executor
from dingo.io import InputArgs


def image_relevant():
    input_data = {
        "eval_group": "test",
        "input_path": "../../test/data/test_img_jsonl.jsonl",  # local filesystem dataset
        "dataset": "local",
        "data_format": "jsonl",
        "save_data": True,
        "save_correct": True,
        "column_id": "id",
        "column_prompt": "url_1",
        "column_content": "url_2",
        "custom_config": {
            "prompt_list": ["PromptImageRelevant"],
            "llm_config": {
                "VLMImageRelevant": {
                    "key": "",
                    "api_url": "",
                }
            }
        }
    }
    input_args = InputArgs(**input_data)
    executor = Executor.exec_map["local"](input_args)
    result = executor.execute()
    print(result)


if __name__ == '__main__':
    image_relevant()
