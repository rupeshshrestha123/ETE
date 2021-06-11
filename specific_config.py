import os

path_to_download = '/content/drive/MyDrive/thesis/english_corpus'
base_model_path = 'model'

os.makedirs(path_to_download, exist_ok=True)
os.makedirs(base_model_path, exist_ok=True)

test_model = base_model_path + 'test'
cache_dir = 'cache'

resume = {
	'restart': False,
	'model_path':
		''
}

use_cuda = False

if not use_cuda:
	num_cuda = '0'
	os.environ["CUDA_VISIBLE_DEVICES"] = num_cuda
else:
	num_cuda = '0'
