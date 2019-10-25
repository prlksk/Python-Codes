def selectionSort(listecan):
   for piril in range(len(listecan)-1,0,-1):
       positionOfMax=0
       for yer in range(1,piril+1):
           if listecan[yer]>listecan[positionOfMax]:
              positionOfMax = yer
        temp=listecan(piril)
        listecan(piril)=listecan(positionOfMax)
        listecan(positionOfMax)=temp
    return listecan
listecan=[54,26,93,17,77,31,44,55,100,20,1]
selectionSort(listecan)
print(selectionSort(listecan))
