My yet to be implemented  search algorithm for the [[Travelling Salesman Problem]].

It's a tree structure with m levels. Each node has n children.
Every node will take the maximum value of it's children (except for the leaves). And eliminate p (p < n) of it's weakest children.

Each iterations removes and regenerates children except for the setup where the tree structure needs to be generated.

The leaves are always going to look in their immediate neighborhood and select the best neighbor and take it's value.

The more levels (m) and children (n) you add the more this will struggle with memory and run time.

Obviously it might not work at all.