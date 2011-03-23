import sys
import mdp, numpy as np
import formats.fs as fs

rows = []
for stats_file in sys.argv[1:]:
    with open(stats_file) as f:
        fs.read_header(f)
        rows.append(fs.read_stats(f))

dataset = np.array(rows)
print np.shape(dataset)

if np.shape(dataset)[0] > 1:
    dataset = (dataset - np.mean(dataset, 0))/np.std(dataset, 0)
    pca = mdp.nodes.PCANode(output_dim=3)
    pca.train(dataset)
    pca.stop_training()

    # TODO: plot samples as biplot in PC1,PC2 space
    
    print 'explained variance:', pca.explained_variance

    v = pca.get_projmatrix()
    print np.shape(v), v

    for x in dataset:
        print 'row:', np.dot(x, v)
else:
    print 'sample:', dataset
