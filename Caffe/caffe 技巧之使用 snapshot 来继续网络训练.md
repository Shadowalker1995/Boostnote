# caffe 技巧之使用 snapshot 来继续网络训练

This is a post summarizing how to resume training on caffe using snapshots.

First, you need to generate snapshot files. You can do this by specify in `solver.prototxt` file. Of course, the name of the solver file is different for different models, usually like `cifar10_quick_solver.prototxt`

```sh
# snapshot intermediate results
snapshot: 500
```

This means that it will take a snapshot every 500 iterations. NOT that it will only take a snapshot at the 500th iteration.

Once you have the snapshots, you will see two files, `model_iter_xxx.caffemodel` and `model_iter_xxx.solverstate` (for example, cifar10_quick_iter_3000.solverstate). The prefix of the filename can be customized in the prototxt file.

Once you have the snapshot, you can specify to use the snapshot in the training script, for cifar10, you can specify in the train_quick.sh with the option 

`--snapshot=cifar10_quick_iter_3000.solverstate`

This will start the training at the 3000th iteration, a note can be found here http://caffe.berkeleyvision.org/gathered/examples/imagenet.html for imagine.

Despite the fact that you only specified the cifar10_quick_iter_3000.solverstate file, to get it actually running, you **ALSO NEED** the cifar10_quick_iter_3000.caffemodel file in the directory.

THERE IS ONE TRICK HERE, the options snapshots and solver have to be specified ON THE SAME LINE, that is don’t miss the “\” after the solver option

```sh
$TOOLS/caffe train \
--solver=examples/cifar10/cifar10_quick_solver.prototxt \
--snapshot=examples/cifar10/cifar10_quick_iter_3000.solverstate
```

OTHERWISE, it WILL NOT start from the snapshot and it won’t tell you what the problem is.

Hope this helps! 
