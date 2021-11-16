import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.sentiment.util import extract_bigram_feats
import json
import networkx as nx
import community as community_louvain
import matplotlib.cm as cm
import matplotlib.pyplot as plt

def get_bigrams(words, top_n, min_freq):
    bcf = BigramCollocationFinder.from_words(iter(words))
    bcf.apply_freq_filter(min_freq)
    bigrams = bcf.nbest(BigramAssocMeasures.pmi, top_n)
    return bigrams

# Opening JSON file
f = open('../data/tweets.json',)

# returns JSON object as
# a dictionary
data = json.load(f)
# Closing file
documents = [d['text'] for d in data]
#documents = documents[:100]
f.close()
print("Number of tweets:"+ str(len (documents)))

doc = ""
for d in documents:
	doc += d+" "	
words = word_tokenize(doc,language='spanish', preserve_line=False)
bigrams = get_bigrams(words,200,3)
#print(bigrams)
# Extract bigram features
matrix = []
for d in documents:
	#print(d)
	matrix.append(extract_bigram_feats(d.split(),bigrams))
#print(matrix)


# Create graph
G = nx.Graph()

for d in range(len(documents)):
	G.add_node(d,tweet=documents[d])
print("Number of nodes:" + str(G.number_of_nodes()))
for d1 in range(len(documents)):
	for d2 in range(len(documents)):
		for bi in bigrams:
			bi_key = "contains("+bi[0]+" - "+bi[1]+")"
			if (matrix[d1][bi_key] and matrix[d2][bi_key]) and (d1!=d2):
				oldEdge = (d1,d2) if (d1,d2) in G.edges else None
				if oldEdge==None:
					G.add_edge(d1,d2,weight=0.1)
				else:
					G.adj[d1][d2]['weight'] += 0.1
print("Number of edges:" + str(G.number_of_edges()))

# compute the best partition
partition = community_louvain.best_partition(G)

# draw the graph
pos = nx.spring_layout(G)
# color the nodes according to their partition
cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=20,
                       cmap=cmap, node_color=list(partition.values()))
nx.draw_networkx_edges(G, pos, alpha=0.5)
nx.write_gexf(G, "test.gexf")
plt.show()