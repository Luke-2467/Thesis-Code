import Rigidity_Functions as RF
'Rigid graph with 4 vertices'
#degree 4
G=[4,[[0,1],[1,2],[2,3], [2,0],[0,3]]]
RF.Run_all(G,"ZZ/101",10)

RF.Genus_Run(G,"ZZ/101","10",[2,0])
#Genus 1

#Taking out outside edges
RF.Genus_Run(G,"ZZ/101","10",[3,0])
#genus 1

#removing [0,2] edge
RF.Genus_Run(G,"ZZ/101","10",[1,0])
#genus 0

RF.Genus_Run(G,"ZZ/101","10",[3,2])
#genus 1

RF.Genus_Run(G,"ZZ/101","10",[1,2],1,2)
#genus -1?

#connecting 3 and 1 now
G=[4,[[0,1],[1,2],[2,3], [3,1],[0,3]]]
RF.Run_all(G,"ZZ/101",10)

RF.Genus_Run(G,"ZZ/101","10",[1,3])
#Genus 1

#Taking out outside edges
RF.Genus_Run(G,"ZZ/101","10",[3,0],3,0)
#genus -1?

#removing [0,2] edge
RF.Genus_Run(G,"ZZ/101","10",[1,0])
#genus 0

RF.Genus_Run(G,"ZZ/101","10",[3,2])
#genus 1

RF.Genus_Run(G,"ZZ/101","10",[1,2])
#genus 1

'Laman graphs with 5 vertices'
G=[5,[[0,1],[1,2],[2,3],[3,0],[3,4],[4,2],[4,1]]]
RF.Run_all(G, "ZZ/101",10)
#degree 8

RF.Genus_Run(G,"ZZ/101","10",[0,1],0,1)
#genus 0
RF.Genus_Run(G,"ZZ/101","10",[1,2],1,2)
#genus 3 or 5

RF.Genus_Run(G,"ZZ/101","10",[1,2],0,1)
#genus 0

RF.Genus_Run(G,"ZZ/101","10",[2,3],0,1)
#genus 5

RF.Genus_Run(G,"ZZ/101","10",[3,0],0,1)
#genus 0

RF.Genus_Run(G,"ZZ/101","10",[3,4])
#genus 5

RF.Genus_Run(G,"ZZ/101","10",[4,2],0,2)
#genus 5

RF.Genus_Run(G,"ZZ/101","10",[4,1], 0,1)
#genus 5
