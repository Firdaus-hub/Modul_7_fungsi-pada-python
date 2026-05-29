def halo (nama):
    print ('halo', nama)
    
def luas_segitiga (alas,tinggi) :
    luas = int ((alas*tinggi)/2)   
    print ('luas segitiga:',luas)
    
def banding  (a,b) :
    if a > b :
        print ('%s > %s'%(a,b))  
    else :
        print ('%s < %s'%(a,b)) 
        
halo ('Daus')  
halo ('Elektromedis')
print ('----------------')   
luas_segitiga (3,7)   
print ('----------------')
banding (8,9)
banding (9,8)       