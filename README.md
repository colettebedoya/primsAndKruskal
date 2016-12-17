# primsAndKruskal
Python prims and kruskal algorithms

Both Prims and Kruskal algorithms are greedy algorithms and both use a minimum spanning tree (MST). They are greedy because they pick the smallest weighted edge that does not cause a cycle in the MST that has been constructed so far.  With Kruskal’s algorithm the first step is that you sort all the edges in non-decreasing order of their weight. The second step is that you then pick the smallest edge.  Then you check to see if the edge forms a cycle with the spanning tree that has been formed so far.  If a cycle is not formed then you include this edge but if it does form a cycle then you discard it.  Then you repeat the second step until all the edges are added to the spanning tree. 
Prim’s algorithm you maintain two sets of vertices.  The first set contains the vertices that are included in the MST and the other set is the vertices that have not yet been added to the MST. This algorithm looks at all the edges that may connect the two sets and picks the vertices with the minimum weight edge. After picking the edge it them moves the other endpoint of the edge to the set containing MST.  With Prim’s the spanning tree means that all vertices must be connected and they must be connected with the minimum weighted edge.

I chose these programs because I feel they are important algorithms to know and learn. They are used in many different applications from games to GPS routing.  I feel like knowing these will benefit me in my job search. 

