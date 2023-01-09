import heapq

class Node:
  def __init__(self, symbol, frequency):
    self.symbol = symbol
    self.frequency = frequency
    self.left = None
    self.right = None
  
  def __lt__(self, other):
    
    return self.frequency < other.frequency

def create_huffman_tree(symbols, frequencies):
  
  nodes = [Node(symbol, frequency) for symbol, frequency in zip(symbols, frequencies)]
  
  
  heapq.heapify(nodes)
  
  while len(nodes) > 1:
    
    left_node = heapq.heappop(nodes)
    right_node = heapq.heappop(nodes)
    
    
    new_node = Node(None, left_node.frequency + right_node.frequency)
    new_node.left = left_node
    new_node.right = right_node
    
    
    heapq.heappush(nodes, new_node)
  
  
  return nodes[0]


symbols = ['A', 'F', '1', '3', '0', 'M', 'T']
frequencies = [0.2, 0.17, 0.13, 0.21, 0.05, 0.09, 0.15]

root = create_huffman_tree(symbols, frequencies)
print(root.symbol)  
print(root.frequency)  
print(root.left.symbol)  
print(root.right.symbol)  

