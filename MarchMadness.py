import random
import numpy as np


def choose(team1 = 'team1',team2 = 'team2',odds = 0.5):
    
    r = random.random()
    
    if r >= odds:
        return team2
    if r < odds:
        return team1


def f64(s1,s2):
    
    x = np.abs(s1-s2)
    
    if s2 > s1:
    
        return 1 - 0.415/(1+(x/9)**5)
    
    if s1 > s2:
        
        return 0.415/(1+(x/9)**5)
    
    if s1 == s2:
        
        print('incorrect seeding (first round)')
        
        return 0.5

def f32(s1,s2):
    
    if s1 < 10 and s2 < 10:
        
        if s2 > s1:
        
            return 1 - 0.33/(1+(s2/8)**8)
        
        if s1 > s2:
            
            return 1 - f32(s2,s1)
        
        if s1 == s2:
            
            print('incorrect seeding (Round of 32)')
            
    
    if s1 >= 10 and s2 < 10 or s1 < 10 and s2 >= 10:
        
        if s2 > s1:
        
            return 1 - 0.33/(1+(s2/11.3)**4)
        
        if s1 > s2:
            
            return 1 - f32(s2,s1)
        
        if s1 == s2:
            
            print('incorrect seeding (Round of 32)')
            
    if s1 >= 10 and s2 >= 10:
        
        if s2 > s1:
            
            return 1 - 0.49/(1+(s2/15.4)**15)
        
        if s1 > s2:
            
            return 1 - f32(s2,s1)
        
        if s1 == s2:
            
            print('incorrect seeding (Round of 32)')
    

        
def f16(s1,s2):
    
    x = np.abs(s2 - s1)
    y = s1 + s2
    
    f = 0.5*(1-3/y)/(1+(x/6)**(12/(((y)**0.5)+(1/2.5)*x**0.5)))
    
    if x == 0:
        
        return 0.5
    
    if x== 1:
        
        if s2 > s1:
            
            return 0.55
        
        if s1 > s2:
            
            return 0.45
        
    if x == 2:
        
        if s1 > 2 and s2 > 2:
            
            if s1 > s2:
            
                return f
            
            if s2 > s1:
                
                return  1 -f 
             
        if s1 == 1 and s2 == 3:
            
            return 0.7
        
        if s1 == 2 and s2 == 4:
            
            return 0.6
        
        else:
            return 1 - f16(s2,s1)
        
    if x > 2:
        
        if s1 == 1 and s2 == 4:
            
            return 0.75
        
        
        
        if s1 > 1 and s2 > 1:
            
            if s1 > s2:
                
                return f
            
            else:
            
                return 1-f


        else:
            
            return 1-f


def createBracket():
    
#first four
    
    FFMW = choose('Arizona State','Nevada')
    FFE = choose('Texas Southern','FDU')
    FFW = choose('Texas A&M-CC','SE Missouri State')
    FFS = choose('Mississippi St.','Pitt')
#west:

    mw1 = 'Kansas'
    mw2 = 'UCLA'
    mw3 = 'Gonzaga'
    mw4 = 'UConn'
    mw5 = 'Saint Marys'
    mw6 = 'TCU'
    mw7 = 'Northwestern'
    mw8 = 'Arkansas'
    mw9 = 'Illinois'
    mw10 = 'Boise St.'
    mw11 = FFMW
    mw12 = 'VCU'
    mw13 = 'Iona'
    mw14 = 'Grand Canyon'
    mw15 = 'UNC Asheville'
    mw16 = 'Howard'
    
#east:
    
    e1 = 'Purdue'
    e2 = 'Marquette'
    e3 = 'Kansas St.'
    e4 = 'Tennessee'
    e5 = 'Duke'
    e6 = 'Kentucky'
    e7 = 'Michigan St.'
    e8 = 'Memphis'
    e9 = 'FAU'
    e10 = 'USC'
    e11 = 'Providence'
    e12 = 'Oral Roberts'
    e13 = 'Louisiana'
    e14 = 'Montana St.'
    e15 = 'Vermont'
    e16 = FFE
    
    w1 = 'Alabama'
    w2 = 'Arizona'
    w3 = 'Baylor'
    w4 = 'Virginia'
    w5 = 'San Diego St.'
    w6 = 'Creighton'
    w7 = 'Missouri'
    w8 = 'Maryland'
    w9 = 'West Virginia'
    w10 = 'Utah St.'
    w11 = 'NC State'
    w12 = 'Col of Charleston'
    w13 = 'Furman'
    w14 = 'UCSB'
    w15 = 'Princeton'
    w16 = FFW
    
    s1 = 'Houston'
    s2 = 'Texas'
    s3 = 'Xavier'
    s4 = 'Indiana'
    s5 = 'Miami (FL)'
    s6 = 'Iowa St.'
    s7 = 'Texas A&M'
    s8 = 'Iowa'
    s9 = 'Auburn'
    s10 = 'Penn St.'
    s11 = FFS
    s12 = 'Drake'
    s13 = 'Kent St.'
    s14 = 'Kennesaw St.'
    s15 = 'Colgate'
    s16 = 'N Kentucky'    

    
    seed_1 = [w1,e1,s1,mw1]
    seed_2 = [w2,e2,s2,mw2]
    seed_3 = [w3,e3,s3,mw3]
    seed_4 = [w4,e4,s4,mw4]
    seed_5 = [w5,e5,s5,mw5]
    seed_6 = [w6,e6,s6,mw6]
    seed_7 = [w7,e7,s7,mw7]
    seed_8 = [w8,e8,s8,mw8]
    seed_9 = [w9,e9,s9,mw9]
    seed_10 = [w10,e10,s10,mw10]
    seed_11 = [w11,e11,s11,mw11]
    seed_12 = [w12,e12,s12,mw12]
    seed_13 = [w13,e13,s13,mw13]
    seed_14 = [w14,e14,s14,mw14]
    seed_15 = [w15,e15,s15,mw15]
    seed_16 = [w16,e16,s16,mw16]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#round of 64 ------------------------------------------------------------------


















    w116 = choose(seed_1[0],seed_16[0],f64(1,16))
    w215 = choose(seed_2[0],seed_15[0],f64(2,15))
    w314 = choose(seed_3[0],seed_14[0],f64(3,14))
    w413 = choose(seed_4[0],seed_13[0],f64(4,13))
    w512 = choose(seed_5[0],seed_12[0],f64(5,12))
    w611 = choose(seed_6[0],seed_11[0],f64(6,11))
    w710 = choose(seed_7[0],seed_10[0],f64(7,10))
    w89 = choose(seed_8[0],seed_9[0],f64(8,9))
    
    e116 = choose(seed_1[1],seed_16[1],f64(1,16))
    e215 = choose(seed_2[1],seed_15[1],f64(2,15))
    e314 = choose(seed_3[1],seed_14[1],f64(3,14))
    e413 = choose(seed_4[1],seed_13[1],f64(4,13))
    e512 = choose(seed_5[1],seed_12[1],f64(5,12))
    e611 = choose(seed_6[1],seed_11[1],f64(6,11))
    e710 = choose(seed_7[1],seed_10[1],f64(7,10))
    e89 = choose(seed_8[1],seed_9[1],f64(8,9))
    
    s116 = choose(seed_1[2],seed_16[2],f64(1,16))
    s215 = choose(seed_2[2],seed_15[2],f64(2,15))
    s314 = choose(seed_3[2],seed_14[2],f64(3,14))
    s413 = choose(seed_4[2],seed_13[2],f64(4,13))
    s512 = choose(seed_5[2],seed_12[2],f64(5,12))
    s611 = choose(seed_6[2],seed_11[2],f64(6,11))
    s710 = choose(seed_7[2],seed_10[2],f64(7,10))
    s89 = choose(seed_8[2],seed_9[2],f64(8,9))
    
    mw116 = choose(seed_1[3],seed_16[3],f64(1,16))
    mw215 = choose(seed_2[3],seed_15[3],f64(2,15))
    mw314 = choose(seed_3[3],seed_14[3],f64(3,14))
    mw413 = choose(seed_4[3],seed_13[3],f64(4,13))
    mw512 = choose(seed_5[3],seed_12[3],f64(5,12))
    mw611 = choose(seed_6[3],seed_11[3],f64(6,11))
    mw710 = choose(seed_7[3],seed_10[3],f64(7,10))
    mw89 = choose(seed_8[3],seed_9[3],f64(8,9))
 
    
 
    
 
    
 
    print('Round of 32:')
    print('...')
    print(w116)
    print(w89)
    print(w512)
    print(w413)
    print(w611)
    print(w314) 
    print(w710)
    print(w215)
    print('.')
    print(e116)
    print(e89)
    print(e512)
    print(e413)
    print(e611)
    print(e314) 
    print(e710)
    print(e215)
    print('.')
    print(s116)
    print(s89)
    print(s512)
    print(s413)
    print(s611)
    print(s314) 
    print(s710)
    print(s215)
    print('.')
    print(mw116)
    print(mw89)
    print(mw512)
    print(mw413)
    print(mw611)
    print(mw314) 
    print(mw710)
    print(mw215)       
    print('...')
 
    
 
    
 
    

    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
#round of 32 ------------------------------------------------------------------































#west






    #sweet sixteen 1

    if w116 == w1:
        
        
        if w89 == w8:
            wss1 = choose(w1,w8,f32(1,8))
        
        if w89 == w9:
            wss1 = choose(w1,w9,f32(1,9))
            

    if w116 == w16:
        
        if w89 == w8:
            wss1 = choose(w16,w8,f32(16,8))
        
        if w89 == w9:
            wss1 = choose(w16,w9,f32(16,9))
                        





    #sweet sixteen 2

    if w215 == w2:
        
        if w710 == w7:
            wss2 = choose(w2,w7,f32(2,7))
        
        if w710 == w10:
            wss2 = choose(w2,w10,f32(2,10))


    if w215 == w15:
        
        if w710 == w7:
            wss2 = choose(w15,w7,f32(15,7))
        
        if w710 == w10:
            wss2 = choose(w15,w10,f32(15,10))
                        



    #sweet sixteen 3

    if w314  == w3:
        
        if w611 == w6:
            wss3 = choose(w3,w6,f32(3,6))
        
        if w611 == w11:
            wss3 = choose(w3,w11,f32(3,11))
            
        
            

    if w314 == w14:
        
        if w611 == w6:
            wss3 = choose(w14,w6,f32(14,6))
        
        if w611 == w11:
            wss3 = choose(w14,w11,f32(14,11))
                        
        
            

    
    #sweet sixteen 4

    if w413 == w4:
        
        if w512 == w5:
            wss4 = choose(w4,w5,f32(4,5))
        
        if w512 == w12:
            wss4 = choose(w4,w12,f32(4,12))
            
        
            

    if w413 == w13:
        
        if w512 == w5:
            wss4 = choose(w13,w5,f32(13,5))
        
        if w512 == w12:
            wss4 = choose(w13,w12,f32(13,12))
                        
        
            






#east





    #sweet sixteen 1

    if e116 == e1:
        
        if e89 == e8:
            ess1 = choose(e1,e8,f32(1,8))
        
        if e89 == e9:
            ess1 = choose(e1,e9,f32(1,9))
            
        
            

    if e116 == e16:
        
        if e89 == e8:
            ess1 = choose(e16,e8,f32(16,8))
        
        if e89 == e9:
            ess1 = choose(e16,e9,f32(16,9))
                        
        
            



    #sweet sixteen 2

    if e215 == e2:
        
        if e710 == e7:
            ess2 = choose(e2,e7,f32(2,7))
        
        if e710 == e10:
            ess2 = choose(e2,e10,f32(2,10))
            
        
            

    if e215 == e15:
        
        if e710 == e7:
            ess2 = choose(e15,e7,f32(15,7))
        
        if e710 == e10:
            ess2 = choose(e15,e10,f32(15,10))
                        
        
            


    #sweet sixteen 3

    if e314  == e3:
        
        if e611 == e6:
            ess3 = choose(e3,e6,f32(3,6))
        
        if e611 == e11:
            ess3 = choose(e3,e11,f32(3,11))
            
        
            

    if e314 == e14:
        
        if e611 == e6:
            ess3 = choose(e14,e6,f32(14,6))
        
        if e611 == e11:
            ess3 = choose(e14,e11,f32(14,11))
                        
        
            


    #sweet sixteen 4

    if e413 == e4:
        
        if e512 == e5:
            ess4 = choose(e4,e5,f32(4,5))
        
        if e512 == e12:
            ess4 = choose(e4,e12,f32(4,12))
            
        
            

    if e413 == e13:
        
        if e512 == e5:
            ess4 = choose(e13,e5,f32(13,5))
        
        if e512 == e12:
            ess4 = choose(e13,e12,f32(13,12))
                        
        
            

    





#south





    #sweet sixteen 1

    if s116 == s1:
        
        if s89 == s8:
            sss1 = choose(s1,s8,f32(1,8))
        
        if s89 == s9:
            sss1 = choose(s1,s9,f32(1,9))
            
        
            

    if s116 == s16:
        
        if s89 == s8:
            sss1 = choose(s16,s8,f32(16,8))
        
        if s89 == s9:
            sss1 = choose(s16,s9,f32(16,9))
                        
        
            


    #sweet sixteen 2

    if s215 == s2:
        
        if s710 == s7:
            sss2 = choose(s2,s7,f32(2,7))
        
        if s710 == s10:
            sss2 = choose(s2,s10,f32(2,10))
            
        
            

    if s215 == s15:
        
        if s710 == s7:
            sss2 = choose(s15,s7,f32(15,7))
        
        if s710 == s10:
            sss2 = choose(s15,s10,f32(15,10))
                        
        
            


    #sweet sixteen 3

    if s314  == s3:
        
        if s611 == s6:
            sss3 = choose(s3,s6,f32(3,6))
        
        if s611 == s11:
            sss3 = choose(s3,s11,f32(3,11))
            
        
            

    if s314 == s14:
        
        if s611 == s6:
            sss3 = choose(s14,s6,f32(14,6))
        
        if s611 == s11:
            sss3 = choose(s14,s11,f32(14,11))
                        
        
            


    #sweet sixteen 4

    if s413 == s4:
        
        if s512 == s5:
            sss4 = choose(s4,s5,f32(4,5))
        
        if s512 == s12:
            sss4 = choose(s4,s12,f32(4,12))
            
        
            

    if s413 == s13:
        
        if s512 == s5:
            sss4 = choose(s13,s5,f32(13,5))
        
        if s512 == s12:
            sss4 = choose(s13,s12,f32(13,12))
                        
        
            







#midwest





    #sweet sixteen 1

    if mw116 == mw1:
        
        if mw89 == mw8:
            mwss1 = choose(mw1,mw8,f32(1,8))
        
        if mw89 == mw9:
            mwss1 = choose(mw1,mw9,f32(1,9))
            
        
            

    if mw116 == mw16:
        
        if mw89 == mw8:
            mwss1 = choose(mw16,mw8,f32(16,8))
        
        if mw89 == mw9:
            mwss1 = choose(mw16,mw9,f32(16,9))
                        
        
            


    #sweet sixteen 2

    if mw215 == mw2:
        
        if mw710 == mw7:
            mwss2 = choose(mw2,mw7,f32(2,7))
        
        if mw710 == mw10:
            mwss2 = choose(mw2,mw10,f32(2,10))
            
        
            

    if mw215 == mw15:
        
        if mw710 == mw7:
            mwss2 = choose(mw15,mw7,f32(15,7))
        
        if mw710 == mw10:
            mwss2 = choose(mw15,mw10,f32(15,10))
                        
        
            


    #sweet sixteen 3

    if mw314  == mw3:
        
        if mw611 == mw6:
            mwss3 = choose(mw3,mw6,f32(3,6))
        
        if mw611 == mw11:
            mwss3 = choose(mw3,mw11,f32(3,11))
            
        
            

    if mw314 == mw14:
        
        if mw611 == mw6:
            mwss3 = choose(mw14,mw6,f32(14,6))
        
        if mw611 == mw11:
            mwss3 = choose(mw14,mw11,f32(14,11))
                        
        
            


    #sweet sixteen 4

    if mw413 == mw4:
        
        if mw512 == mw5:
            mwss4 = choose(mw4,mw5,f32(4,5))
        
        if mw512 == mw12:
            mwss4 = choose(mw4,mw12,f32(4,12))
            
        
            

    if mw413 == mw13:
        
        if mw512 == mw5:
            mwss4 = choose(mw13,mw5,f32(13,5))
        
        if mw512 == mw12:
            mwss4 = choose(mw13,mw12,f32(13,12))
                        
        
            











    print('Sweet Sixteen')
    print('...')
    print(wss1)
    print(wss4)
    print(wss3)
    print(wss2)
    print('.')
    print(ess1)
    print(ess4)
    print(ess3)
    print(ess2)
    print('.')
    print(sss1)
    print(sss4)
    print(sss3)
    print(sss2)
    print('.')
    print(mwss1)
    print(mwss4)
    print(mwss3)
    print(mwss2)
    print('...')























#sweet 16 ------------------------------------------------------------------

































#west





    #elite eight 1

    if wss1 == w1:
        
        if wss4 == w4:
            wee1 = choose(w1,w4,f16(1,4))
        
        if wss4 == w5:
            wee1 = choose(w1,w5,f16(1,5))
        
        if wss4 == w12:
            wee1 = choose(w1,w12,f16(1,12))      
        
        if wss4 == w13:
            wee1 = choose(w1,w13,f16(1,13))
            
        
            

    if wss1 == w8:
        
        if wss4 == w4:
            wee1 = choose(w8,w4,f16(8,4))
        
        if wss4 == w5:
            wee1 = choose(w8,w5,f16(8,5))
        
        if wss4 == w12:
            wee1 = choose(w8,w12,f16(8,12))      
        
        if wss4 == w13:
            wee1 = choose(w8,w13,f16(8,13))
            
        
            

    if wss1 == w9:
        
        if wss4 == w4:
            wee1 = choose(w9,w4,f16(9,4))
        
        if wss4 == w5:
            wee1 = choose(w9,w5,f16(9,5))
        
        if wss4 == w12:
            wee1 = choose(w9,w12,f16(9,12))      
        
        if wss4 == w13:
            wee1 = choose(w9,w13,f16(9,13))
            
        
            

    if wss1 == w16:
        
        if wss4 == w4:
            wee1 = choose(w16,w4,f16(16,4))
        
        if wss4 == w5:
            wee1 = choose(w16,w5,f16(16,5))
        
        if wss4 == w12:
            wee1 = choose(w16,w12,f16(16,12))      
        
        if wss4 == w13:
            wee1 = choose(w16,w13,f16(16,13))
            
        
            


    #elite eight 2

    if wss2 == w2:
        
        if wss3 == w3:
            wee2 = choose(w2,w3,f16(2,3))
        
        if wss3 == w6:
            wee2 = choose(w2,w6,f16(2,6))
        
        if wss3 == w11:
            wee2 = choose(w2,w11,f16(2,11))      
        
        if wss3 == w14:
            wee2 = choose(w2,w14,f16(2,14))
            
        
            

    if wss2 == w7:
        
        if wss3 == w3:
            wee2 = choose(w7,w3,f16(7,3))
        
        if wss3 == w6:
            wee2 = choose(w7,w6,f16(7,6))
        
        if wss3 == w11:
            wee2 = choose(w7,w11,f16(7,11))      
        
        if wss3 == w14:
            wee2 = choose(w7,w14,f16(7,14))
            
        
            

    if wss2 == w10:
        
        if wss3 == w3:
            wee2 = choose(w10,w3,f16(10,3))
        
        if wss3 == w6:
            wee2 = choose(w10,w6,f16(10,6))
        
        if wss3 == w11:
            wee2 = choose(w10,w11,f16(10,11))      
        
        if wss3 == w14:
            wee2 = choose(w10,w14,f16(10,14))
            
        
            

    if wss2 == w15:
        
        if wss3 == w3:
            wee2 = choose(w15,w3,f16(15,3))
        
        if wss3 == w6:
            wee2 = choose(w15,w6,f16(15,6))
        
        if wss3 == w11:
            wee2 = choose(w15,w11,f16(15,11))      
        
        if wss3 == w14:
            wee2 = choose(w15,w14,f16(15,14))
            
        
            











#east



    #elite eight 1

    if ess1 == e1:
        
        if ess4 == e4:
            eee1 = choose(e1,e4,f16(1,4))
        
        if ess4 == e5:
            eee1 = choose(e1,e5,f16(1,5))
        
        if ess4 == e12:
            eee1 = choose(e1,e12,f16(1,12))      
        
        if ess4 == e13:
            eee1 = choose(e1,e13,f16(1,13))
            
        
            

    if ess1 == e8:
        
        if ess4 == e4:
            eee1 = choose(e8,e4,f16(8,4))
        
        if ess4 == e5:
            eee1 = choose(e8,e5,f16(8,5))
        
        if ess4 == e12:
            eee1 = choose(e8,e12,f16(8,12))      
        
        if ess4 == e13:
            eee1 = choose(e8,e13,f16(8,13))
            
        
            

    if ess1 == e9:
        
        if ess4 == e4:
            eee1 = choose(e9,e4,f16(9,4))
        
        if ess4 == e5:
            eee1 = choose(e9,e5,f16(9,5))
        
        if ess4 == e12:
            eee1 = choose(e9,e12,f16(9,12))      
        
        if ess4 == e13:
            eee1 = choose(e9,e13,f16(9,13))
            
        
            

    if ess1 == e16:
        
        if ess4 == e4:
            eee1 = choose(e16,e4,f16(16,4))
        
        if ess4 == e5:
            eee1 = choose(e16,e5,f16(16,5))
        
        if ess4 == e12:
            eee1 = choose(e16,e12,f16(16,12))      
        
        if ess4 == e13:
            eee1 = choose(e16,e13,f16(16,13))
            
        
            


    #elite eight 2

    if ess2 == e2:
        
        if ess3 == e3:
            eee2 = choose(e2,e3,f16(2,3))
        
        if ess3 == e6:
            eee2 = choose(e2,e6,f16(2,6))
        
        if ess3 == e11:
            eee2 = choose(e2,e11,f16(2,11))      
        
        if ess3 == e14:
            eee2 = choose(e2,e14,f16(2,14))
            
        
            

    if ess2 == e7:
        
        if ess3 == e3:
            eee2 = choose(e7,e3,f16(7,3))
        
        if ess3 == e6:
            eee2 = choose(e7,e6,f16(7,6))
        
        if ess3 == e11:
            eee2 = choose(e7,e11,f16(7,11))      
        
        if ess3 == e14:
            eee2 = choose(e7,e14,f16(7,14))
            
        
            

    if ess2 == e10:
        
        if ess3 == e3:
            eee2 = choose(e10,e3,f16(10,3))
        
        if ess3 == e6:
            eee2 = choose(e10,e6,f16(10,6))
        
        if ess3 == e11:
            eee2 = choose(e10,e11,f16(10,11))      
        
        if ess3 == e14:
            eee2 = choose(e10,e14,f16(10,14))
            
        
            

    if ess2 == e15:
        
        if ess3 == e3:
            eee2 = choose(e15,e3,f16(15,3))
        
        if ess3 == e6:
            eee2 = choose(e15,e6,f16(15,6))
        
        if ess3 == e11:
            eee2 = choose(e15,e11,f16(15,11))      
        
        if ess3 == e14:
            eee2 = choose(e15,e14,f16(15,14))
            
        
            









#south





    #elite eight 1

    if sss1 == s1:
        
        if sss4 == s4:
            see1 = choose(s1,s4,f16(1,4))
        
        if sss4 == s5:
            see1 = choose(s1,s5,f16(1,5))
        
        if sss4 == s12:
            see1 = choose(s1,s12,f16(1,12))      
        
        if sss4 == s13:
            see1 = choose(s1,s13,f16(1,13))
            
        
            

    if sss1 == s8:
        
        if sss4 == s4:
            see1 = choose(s8,s4,f16(8,4))
        
        if sss4 == s5:
            see1 = choose(s8,s5,f16(8,5))
        
        if sss4 == s12:
            see1 = choose(s8,s12,f16(8,12))      
        
        if sss4 == s13:
            see1 = choose(s8,s13,f16(8,13))
            
        
            

    if sss1 == s9:
        
        if sss4 == s4:
            see1 = choose(s9,s4,f16(9,4))
        
        if sss4 == s5:
            see1 = choose(s9,s5,f16(9,5))
        
        if sss4 == s12:
            see1 = choose(s9,s12,f16(9,12))      
        
        if sss4 == s13:
            see1 = choose(s9,s13,f16(9,13))
            
        
            

    if sss1 == s16:
        
        if sss4 == s4:
            see1 = choose(s16,s4,f16(16,4))
        
        if sss4 == s5:
            see1 = choose(s16,s5,f16(16,5))
        
        if sss4 == s12:
            see1 = choose(s16,s12,f16(16,12))      
        
        if sss4 == s13:
            see1 = choose(s16,s13,f16(16,13))
            
        
            


    #elite eight 2

    if sss2 == s2:
        
        if sss3 == s3:
            see2 = choose(s2,s3,f16(2,3))
        
        if sss3 == s6:
            see2 = choose(s2,s6,f16(2,6))
        
        if sss3 == s11:
            see2 = choose(s2,s11,f16(2,11))      
        
        if sss3 == s14:
            see2 = choose(s2,s14,f16(2,14))
            
        
            

    if sss2 == s7:
        
        if sss3 == s3:
            see2 = choose(s7,s3,f16(7,3))
        
        if sss3 == s6:
            see2 = choose(s7,s6,f16(7,6))
        
        if sss3 == s11:
            see2 = choose(s7,s11,f16(7,11))      
        
        if sss3 == s14:
            see2 = choose(s7,s14,f16(7,14))
            
        
            

    if sss2 == s10:
        
        if sss3 == s3:
            see2 = choose(s10,s3,f16(10,3))
        
        if sss3 == s6:
            see2 = choose(s10,s6,f16(10,6))
        
        if sss3 == s11:
            see2 = choose(s10,s11,f16(10,11))      
        
        if sss3 == s14:
            see2 = choose(s10,s14,f16(10,14))
            
        
            

    if sss2 == s15:
        
        if sss3 == s3:
            see2 = choose(s15,s3,f16(15,3))
        
        if sss3 == s6:
            see2 = choose(s15,s6,f16(15,6))
        
        if sss3 == s11:
            see2 = choose(s15,s11,f16(15,11))      
        
        if sss3 == s14:
            see2 = choose(s15,s14,f16(15,14))
            
        
            






#midwest





    #elite eight 1

    if mwss1 == mw1:
        
        if mwss4 == mw4:
            mwee1 = choose(mw1,mw4,f16(1,4))
        
        if mwss4 == mw5:
            mwee1 = choose(mw1,mw5,f16(1,5))
        
        if mwss4 == mw12:
            mwee1 = choose(mw1,mw12,f16(1,12))      
        
        if mwss4 == mw13:
            mwee1 = choose(mw1,mw13,f16(1,13))
            
        
            

    if mwss1 == mw8:
        
        if mwss4 == mw4:
            mwee1 = choose(mw8,mw4,f16(8,4))
        
        if mwss4 == mw5:
            mwee1 = choose(mw8,mw5,f16(8,5))
        
        if mwss4 == mw12:
            mwee1 = choose(mw8,mw12,f16(8,12))      
        
        if mwss4 == mw13:
            mwee1 = choose(mw8,mw13,f16(8,13))
            
        
            

    if mwss1 == mw9:
        
        if mwss4 == mw4:
            mwee1 = choose(mw9,mw4,f16(9,4))
        
        if mwss4 == mw5:
            mwee1 = choose(mw9,mw5,f16(9,5))
        
        if mwss4 == mw12:
            mwee1 = choose(mw9,mw12,f16(9,12))      
        
        if mwss4 == mw13:
            mwee1 = choose(mw9,mw13,f16(9,13))
            
        
            

    if mwss1 == mw16:
        
        if mwss4 == mw4:
            mwee1 = choose(mw16,mw4,f16(16,4))
        
        if mwss4 == mw5:
            mwee1 = choose(mw16,mw5,f16(16,5))
        
        if mwss4 == mw12:
            mwee1 = choose(mw16,mw12,f16(16,12))      
        
        if mwss4 == mw13:
            mwee1 = choose(mw16,mw13,f16(16,13))
            
        
            


    #elite eight 2

    if mwss2 == mw2:
        
        if mwss3 == mw3:
            mwee2 = choose(mw2,mw3,f16(2,3))
        
        if mwss3 == mw6:
            mwee2 = choose(mw2,mw6,f16(2,6))
        
        if mwss3 == mw11:
            mwee2 = choose(mw2,mw11,f16(2,11))      
        
        if mwss3 == mw14:
            mwee2 = choose(mw2,mw14,f16(2,14))
            
        
            

    if mwss2 == mw7:
        
        if mwss3 == mw3:
            mwee2 = choose(mw7,mw3,f16(7,3))
        
        if mwss3 == mw6:
            mwee2 = choose(mw7,mw6,f16(7,6))
        
        if mwss3 == mw11:
            mwee2 = choose(mw7,mw11,f16(7,11))      
        
        if mwss3 == mw14:
            mwee2 = choose(mw7,mw14,f16(7,14))
            
        
            

    if mwss2 == mw10:
        
        if mwss3 == mw3:
            mwee2 = choose(mw10,mw3,f16(10,3))
        
        if mwss3 == mw6:
            mwee2 = choose(mw10,mw6,f16(10,6))
        
        if mwss3 == mw11:
            mwee2 = choose(mw10,mw11,f16(10,11))      
        
        if mwss3 == mw14:
            mwee2 = choose(mw10,mw14,f16(10,14))
            
        
            

    if mwss2 == mw15:
        
        if mwss3 == mw3:
            mwee2 = choose(mw15,mw3,f16(15,3))
        
        if mwss3 == mw6:
            mwee2 = choose(mw15,mw6,f16(15,6))
        
        if mwss3 == mw11:
            mwee2 = choose(mw15,mw11,f16(15,11))      
        
        if mwss3 == mw14:
            mwee2 = choose(mw15,mw14,f16(15,14))
            
        
            






    print('Elite Eight:')
    print('...')
    print(wee1)
    print(wee2)
    print(eee1)
    print(eee2)
    print('.')
    print(see1)
    print(see2)
    print(mwee1)
    print(mwee2)
    print('...')









































#elite eight ------------------------------------------------------------------






























#west





    #final four

    if wee1 == w1:
        
        if wee2 == w2:
            wff = choose(w1,w2,f16(1,2))
        
        if wee2 == w3:
            wff = choose(w1,w3,f16(1,3))
        
        if wee2 == w6:
            wff = choose(w1,w6,f16(1,6))      
        
        if wee2 == w7:
            wff = choose(w1,w7,f16(1,7))
            
        if wee2 == w10:
            wff = choose(w1,w10,f16(1,10))
        
        if wee2 == w11:
            wff = choose(w1,w11,f16(1,11))
        
        if wee2 == w14:
            wff = choose(w1,w14,f16(1,14))      
        
        if wee2 == w15:
            wff = choose(w1,w15,f16(1,15))
        
            

    if wee1 == w4:
        
        if wee2 == w2:
            wff = choose(w4,w2,f16(4,2))
        
        if wee2 == w3:
            wff = choose(w4,w3,f16(4,3))
        
        if wee2 == w6:
            wff = choose(w4,w6,f16(4,6))      
        
        if wee2 == w7:
            wff = choose(w4,w7,f16(4,7))
            
        if wee2 == w10:
            wff = choose(w4,w10,f16(4,10))
        
        if wee2 == w11:
            wff = choose(w4,w11,f16(4,11))
        
        if wee2 == w14:
            wff = choose(w4,w14,f16(4,14))      
        
        if wee2 == w15:
            wff = choose(w4,w15,f16(4,15))
            
        
            

    if wee1 == w5:
        
        if wee2 == w2:
            wff = choose(w5,w2,f16(5,2))
        
        if wee2 == w3:
            wff = choose(w5,w3,f16(5,3))
        
        if wee2 == w6:
            wff = choose(w5,w6,f16(5,6))      
        
        if wee2 == w7:
            wff = choose(w5,w7,f16(5,7))
            
        if wee2 == w10:
            wff = choose(w5,w10,f16(5,10))
        
        if wee2 == w11:
            wff = choose(w5,w11,f16(5,11))
        
        if wee2 == w14:
            wff = choose(w5,w14,f16(5,14))      
        
        if wee2 == w15:
            wff = choose(w5,w15,f16(5,15))
            
        
            
            
    if wee1 == w8:
        
        if wee2 == w2:
            wff = choose(w8,w2,f16(8,2))
        
        if wee2 == w3:
            wff = choose(w8,w3,f16(8,3))
        
        if wee2 == w6:
            wff = choose(w8,w6,f16(8,6))      
        
        if wee2 == w7:
            wff = choose(w8,w7,f16(8,7))
            
        if wee2 == w10:
            wff = choose(w8,w10,f16(8,10))
        
        if wee2 == w11:
            wff = choose(w8,w11,f16(8,11))
        
        if wee2 == w14:
            wff = choose(w8,w14,f16(8,14))      
        
        if wee2 == w15:
            wff = choose(w8,w15,f16(8,15))
            
        
            
            
    if wee1 == w9:
        
        if wee2 == w2:
            wff = choose(w9,w2,f16(9,2))
        
        if wee2 == w3:
            wff = choose(w9,w3,f16(9,3))
        
        if wee2 == w6:
            wff = choose(w9,w6,f16(9,6))      
        
        if wee2 == w7:
            wff = choose(w9,w7,f16(9,7))
            
        if wee2 == w10:
            wff = choose(w9,w10,f16(9,10))
        
        if wee2 == w11:
            wff = choose(w9,w11,f16(9,11))
        
        if wee2 == w14:
            wff = choose(w9,w14,f16(9,14))      
        
        if wee2 == w15:
            wff = choose(w9,w15,f16(9,15))
            
        
            
            
    if wee1 == w12:
        
        if wee2 == w2:
            wff = choose(w12,w2,f16(12,2))
        
        if wee2 == w3:
            wff = choose(w12,w3,f16(12,3))
        
        if wee2 == w6:
            wff = choose(w12,w6,f16(12,6))      
        
        if wee2 == w7:
            wff = choose(w12,w7,f16(12,7))
            
        if wee2 == w10:
            wff = choose(w12,w10,f16(12,10))
        
        if wee2 == w11:
            wff = choose(w12,w11,f16(12,11))
        
        if wee2 == w14:
            wff = choose(w12,w14,f16(12,14))      
        
        if wee2 == w15:
            wff = choose(w12,w15,f16(12,15))
            
        
            
            
    if wee1 == w13:
        
        if wee2 == w2:
            wff = choose(w13,w2,f16(13,2))
        
        if wee2 == w3:
            wff = choose(w13,w3,f16(13,3))
        
        if wee2 == w6:
            wff = choose(w13,w6,f16(13,6))      
        
        if wee2 == w7:
            wff = choose(w13,w7,f16(13,7))
            
        if wee2 == w10:
            wff = choose(w13,w10,f16(13,10))
        
        if wee2 == w11:
            wff = choose(w13,w11,f16(13,11))
        
        if wee2 == w14:
            wff = choose(w13,w14,f16(13,14))      
        
        if wee2 == w15:
            wff = choose(w13,w15,f16(13,15))
            
        
            
            
    if wee1 == w16:
        
        if wee2 == w2:
            wff = choose(w16,w2,f16(16,2))
        
        if wee2 == w3:
            wff = choose(w16,w3,f16(16,3))
        
        if wee2 == w6:
            wff = choose(w16,w6,f16(16,6))      
        
        if wee2 == w7:
            wff = choose(w16,w7,f16(16,7))
            
        if wee2 == w10:
            wff = choose(w16,w10,f16(16,10))
        
        if wee2 == w11:
            wff = choose(w16,w11,f16(16,11))
        
        if wee2 == w14:
            wff = choose(w16,w14,f16(16,14))      
        
        if wee2 == w15:
            wff = choose(w16,w15,f16(16,15))
            
        
            
            
            
            
            











#east





    #final four

    if eee1 == e1:
        
        if eee2 == e2:
            eff = choose(e1,e2,f16(1,2))
        
        if eee2 == e3:
            eff = choose(e1,e3,f16(1,3))
        
        if eee2 == e6:
            eff = choose(e1,e6,f16(1,6))      
        
        if eee2 == e7:
            eff = choose(e1,e7,f16(1,7))
            
        if eee2 == e10:
            eff = choose(e1,e10,f16(1,10))
        
        if eee2 == e11:
            eff = choose(e1,e11,f16(1,11))
        
        if eee2 == e14:
            eff = choose(e1,e14,f16(1,14))      
        
        if eee2 == e15:
            eff = choose(e1,e15,f16(1,15))
        
            

    if eee1 == e4:
        
        if eee2 == e2:
            eff = choose(e4,e2,f16(4,2))
        
        if eee2 == e3:
            eff = choose(e4,e3,f16(4,3))
        
        if eee2 == e6:
            eff = choose(e4,e6,f16(4,6))      
        
        if eee2 == e7:
            eff = choose(e4,e7,f16(4,7))
            
        if eee2 == e10:
            eff = choose(e4,e10,f16(4,10))
        
        if eee2 == e11:
            eff = choose(e4,e11,f16(4,11))
        
        if eee2 == e14:
            eff = choose(e4,e14,f16(4,14))      
        
        if eee2 == e15:
            eff = choose(e4,e15,f16(4,15))
            
        
            

    if eee1 == e5:
        
        if eee2 == e2:
            eff = choose(e5,e2,f16(5,2))
        
        if eee2 == e3:
            eff = choose(e5,e3,f16(5,3))
        
        if eee2 == e6:
            eff = choose(e5,e6,f16(5,6))      
        
        if eee2 == e7:
            eff = choose(e5,e7,f16(5,7))
            
        if eee2 == e10:
            eff = choose(e5,e10,f16(5,10))
        
        if eee2 == e11:
            eff = choose(e5,e11,f16(5,11))
        
        if eee2 == e14:
            eff = choose(e5,e14,f16(5,14))      
        
        if eee2 == e15:
            eff = choose(e5,e15,f16(5,15))
            
        
            
            
    if eee1 == e8:
        
        if eee2 == e2:
            eff = choose(e8,e2,f16(8,2))
        
        if eee2 == e3:
            eff = choose(e8,e3,f16(8,3))
        
        if eee2 == e6:
            eff = choose(e8,e6,f16(8,6))      
        
        if eee2 == e7:
            eff = choose(e8,e7,f16(8,7))
            
        if eee2 == e10:
            eff = choose(e8,e10,f16(8,10))
        
        if eee2 == e11:
            eff = choose(e8,e11,f16(8,11))
        
        if eee2 == e14:
            eff = choose(e8,e14,f16(8,14))      
        
        if eee2 == e15:
            eff = choose(e8,e15,f16(8,15))
            
        
            
            
    if eee1 == e9:
        
        if eee2 == e2:
            eff = choose(e9,e2,f16(9,2))
        
        if eee2 == e3:
            eff = choose(e9,e3,f16(9,3))
        
        if eee2 == e6:
            eff = choose(e9,e6,f16(9,6))      
        
        if eee2 == e7:
            eff = choose(e9,e7,f16(9,7))
            
        if eee2 == e10:
            eff = choose(e9,e10,f16(9,10))
        
        if eee2 == e11:
            eff = choose(e9,e11,f16(9,11))
        
        if eee2 == e14:
            eff = choose(e9,e14,f16(9,14))      
        
        if eee2 == e15:
            eff = choose(e9,e15,f16(9,15))
            
        
            
            
    if eee1 == e12:
        
        if eee2 == e2:
            eff = choose(e12,e2,f16(12,2))
        
        if eee2 == e3:
            eff = choose(e12,e3,f16(12,3))
        
        if eee2 == e6:
            eff = choose(e12,e6,f16(12,6))      
        
        if eee2 == e7:
            eff = choose(e12,e7,f16(12,7))
            
        if eee2 == e10:
            eff = choose(e12,e10,f16(12,10))
        
        if eee2 == e11:
            eff = choose(e12,e11,f16(12,11))
        
        if eee2 == e14:
            eff = choose(e12,e14,f16(12,14))      
        
        if eee2 == e15:
            eff = choose(e12,e15,f16(12,15))
            
        
            
            
    if eee1 == e13:
        
        if eee2 == e2:
            eff = choose(e13,e2,f16(13,2))
        
        if eee2 == e3:
            eff = choose(e13,e3,f16(13,3))
        
        if eee2 == e6:
            eff = choose(e13,e6,f16(13,6))      
        
        if eee2 == e7:
            eff = choose(e13,e7,f16(13,7))
            
        if eee2 == e10:
            eff = choose(e13,e10,f16(13,10))
        
        if eee2 == e11:
            eff = choose(e13,e11,f16(13,11))
        
        if eee2 == e14:
            eff = choose(e13,e14,f16(13,14))      
        
        if eee2 == e15:
            eff = choose(e13,e15,f16(13,15))
            
        
            
            
    if eee1 == e16:
        
        if eee2 == e2:
            eff = choose(e16,e2,f16(16,2))
        
        if eee2 == e3:
            eff = choose(e16,e3,f16(16,3))
        
        if eee2 == e6:
            eff = choose(e16,e6,f16(16,6))      
        
        if eee2 == e7:
            eff = choose(e16,e7,f16(16,7))
            
        if eee2 == e10:
            eff = choose(e16,e10,f16(16,10))
        
        if eee2 == e11:
            eff = choose(e16,e11,f16(16,11))
        
        if eee2 == e14:
            eff = choose(e16,e14,f16(16,14))      
        
        if eee2 == e15:
            eff = choose(e16,e15,f16(16,15))
            
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        
        
#south





    #final four

    if see1 == s1:
        
        if see2 == s2:
            sff = choose(s1,s2,f16(1,2))
        
        if see2 == s3:
            sff = choose(s1,s3,f16(1,3))
        
        if see2 == s6:
            sff = choose(s1,s6,f16(1,6))      
        
        if see2 == s7:
            sff = choose(s1,s7,f16(1,7))
            
        if see2 == s10:
            sff = choose(s1,s10,f16(1,10))
        
        if see2 == s11:
            sff = choose(s1,s11,f16(1,11))
        
        if see2 == s14:
            sff = choose(s1,s14,f16(1,14))      
        
        if see2 == s15:
            sff = choose(s1,s15,f16(1,15))
        
            

    if see1 == s4:
        
        if see2 == s2:
            sff = choose(s4,s2,f16(4,2))
        
        if see2 == s3:
            sff = choose(s4,s3,f16(4,3))
        
        if see2 == s6:
            sff = choose(s4,s6,f16(4,6))      
        
        if see2 == s7:
            sff = choose(s4,s7,f16(4,7))
            
        if see2 == s10:
            sff = choose(s4,s10,f16(4,10))
        
        if see2 == s11:
            sff = choose(s4,s11,f16(4,11))
        
        if see2 == s14:
            sff = choose(s4,s14,f16(4,14))      
        
        if see2 == s15:
            sff = choose(s4,s15,f16(4,15))
            
        
            

    if see1 == s5:
        
        if see2 == s2:
            sff = choose(s5,s2,f16(5,2))
        
        if see2 == s3:
            sff = choose(s5,s3,f16(5,3))
        
        if see2 == s6:
            sff = choose(s5,s6,f16(5,6))      
        
        if see2 == s7:
            sff = choose(s5,s7,f16(5,7))
            
        if see2 == s10:
            sff = choose(s5,s10,f16(5,10))
        
        if see2 == s11:
            sff = choose(s5,s11,f16(5,11))
        
        if see2 == s14:
            sff = choose(s5,s14,f16(5,14))      
        
        if see2 == s15:
            sff = choose(s5,s15,f16(5,15))
            
        
            
            
    if see1 == s8:
        
        if see2 == s2:
            sff = choose(s8,s2,f16(8,2))
        
        if see2 == s3:
            sff = choose(s8,s3,f16(8,3))
        
        if see2 == s6:
            sff = choose(s8,s6,f16(8,6))      
        
        if see2 == s7:
            sff = choose(s8,s7,f16(8,7))
            
        if see2 == s10:
            sff = choose(s8,s10,f16(8,10))
        
        if see2 == s11:
            sff = choose(s8,s11,f16(8,11))
        
        if see2 == s14:
            sff = choose(s8,s14,f16(8,14))      
        
        if see2 == s15:
            sff = choose(s8,s15,f16(8,15))
            
        
            
            
    if see1 == s9:
        
        if see2 == s2:
            sff = choose(s9,s2,f16(9,2))
        
        if see2 == s3:
            sff = choose(s9,s3,f16(9,3))
        
        if see2 == s6:
            sff = choose(s9,s6,f16(9,6))      
        
        if see2 == s7:
            sff = choose(s9,s7,f16(9,7))
            
        if see2 == s10:
            sff = choose(s9,s10,f16(9,10))
        
        if see2 == s11:
            sff = choose(s9,s11,f16(9,11))
        
        if see2 == s14:
            sff = choose(s9,s14,f16(9,14))      
        
        if see2 == s15:
            sff = choose(s9,s15,f16(9,15))
            
        
            
            
    if see1 == s12:
        
        if see2 == s2:
            sff = choose(s12,s2,f16(12,2))
        
        if see2 == s3:
            sff = choose(s12,s3,f16(12,3))
        
        if see2 == s6:
            sff = choose(s12,s6,f16(12,6))      
        
        if see2 == s7:
            sff = choose(s12,s7,f16(12,7))
            
        if see2 == s10:
            sff = choose(s12,s10,f16(12,10))
        
        if see2 == s11:
            sff = choose(s12,s11,f16(12,11))
        
        if see2 == s14:
            sff = choose(s12,s14,f16(12,14))      
        
        if see2 == s15:
            sff = choose(s12,s15,f16(12,15))
            
        
            
            
    if see1 == s13:
        
        if see2 == s2:
            sff = choose(s13,s2,f16(13,2))
        
        if see2 == s3:
            sff = choose(s13,s3,f16(13,3))
        
        if see2 == s6:
            sff = choose(s13,s6,f16(13,6))      
        
        if see2 == s7:
            sff = choose(s13,s7,f16(13,7))
            
        if see2 == s10:
            sff = choose(s13,s10,f16(13,10))
        
        if see2 == s11:
            sff = choose(s13,s11,f16(13,11))
        
        if see2 == s14:
            sff = choose(s13,s14,f16(13,14))      
        
        if see2 == s15:
            sff = choose(s13,s15,f16(13,15))
            
        
            
            
    if see1 == s16:
        
        if see2 == s2:
            sff = choose(s16,s2,f16(16,2))
        
        if see2 == s3:
            sff = choose(s16,s3,f16(16,3))
        
        if see2 == s6:
            sff = choose(s16,s6,f16(16,6))      
        
        if see2 == s7:
            sff = choose(s16,s7,f16(16,7))
            
        if see2 == s10:
            sff = choose(s16,s10,f16(16,10))
        
        if see2 == s11:
            sff = choose(s16,s11,f16(16,11))
        
        if see2 == s14:
            sff = choose(s16,s14,f16(16,14))      
        
        if see2 == s15:
            sff = choose(s16,s15,f16(16,15))
            
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
#midwest





    #final four

    if mwee1 == mw1:
        
        if mwee2 == mw2:
            mwff = choose(mw1,mw2,f16(1,2))
        
        if mwee2 == mw3:
            mwff = choose(mw1,mw3,f16(1,3))
        
        if mwee2 == mw6:
            mwff = choose(mw1,mw6,f16(1,6))      
        
        if mwee2 == mw7:
            mwff = choose(mw1,mw7,f16(1,7))
            
        if mwee2 == mw10:
            mwff = choose(mw1,mw10,f16(1,10))
        
        if mwee2 == mw11:
            mwff = choose(mw1,mw11,f16(1,11))
        
        if mwee2 == mw14:
            mwff = choose(mw1,mw14,f16(1,14))      
        
        if mwee2 == mw15:
            mwff = choose(mw1,mw15,f16(1,15))
        
            

    if mwee1 == mw4:
        
        if mwee2 == mw2:
            mwff = choose(mw4,mw2,f16(4,2))
        
        if mwee2 == mw3:
            mwff = choose(mw4,mw3,f16(4,3))
        
        if mwee2 == mw6:
            mwff = choose(mw4,mw6,f16(4,6))      
        
        if mwee2 == mw7:
            mwff = choose(mw4,mw7,f16(4,7))
            
        if mwee2 == mw10:
            mwff = choose(mw4,mw10,f16(4,10))
        
        if mwee2 == mw11:
            mwff = choose(mw4,mw11,f16(4,11))
        
        if mwee2 == mw14:
            mwff = choose(mw4,mw14,f16(4,14))      
        
        if mwee2 == mw15:
            mwff = choose(mw4,mw15,f16(4,15))
            
        
            

    if mwee1 == mw5:
        
        if mwee2 == mw2:
            mwff = choose(mw5,mw2,f16(5,2))
        
        if mwee2 == mw3:
            mwff = choose(mw5,mw3,f16(5,3))
        
        if mwee2 == mw6:
            mwff = choose(mw5,mw6,f16(5,6))      
        
        if mwee2 == mw7:
            mwff = choose(mw5,mw7,f16(5,7))
            
        if mwee2 == mw10:
            mwff = choose(mw5,mw10,f16(5,10))
        
        if mwee2 == mw11:
            mwff = choose(mw5,mw11,f16(5,11))
        
        if mwee2 == mw14:
            mwff = choose(mw5,mw14,f16(5,14))      
        
        if mwee2 == mw15:
            mwff = choose(mw5,mw15,f16(5,15))
            
        
            
            
    if mwee1 == mw8:
        
        if mwee2 == mw2:
            mwff = choose(mw8,mw2,f16(8,2))
        
        if mwee2 == mw3:
            mwff = choose(mw8,mw3,f16(8,3))
        
        if mwee2 == mw6:
            mwff = choose(mw8,mw6,f16(8,6))      
        
        if mwee2 == mw7:
            mwff = choose(mw8,mw7,f16(8,7))
            
        if mwee2 == mw10:
            mwff = choose(mw8,mw10,f16(8,10))
        
        if mwee2 == mw11:
            mwff = choose(mw8,mw11,f16(8,11))
        
        if mwee2 == mw14:
            mwff = choose(mw8,mw14,f16(8,14))      
        
        if mwee2 == mw15:
            mwff = choose(mw8,mw15,f16(8,15))
            
        
            
            
    if mwee1 == mw9:
        
        if mwee2 == mw2:
            mwff = choose(mw9,mw2,f16(9,2))
        
        if mwee2 == mw3:
            mwff = choose(mw9,mw3,f16(9,3))
        
        if mwee2 == mw6:
            mwff = choose(mw9,mw6,f16(9,6))      
        
        if mwee2 == mw7:
            mwff = choose(mw9,mw7,f16(9,7))
            
        if mwee2 == mw10:
            mwff = choose(mw9,mw10,f16(9,10))
        
        if mwee2 == mw11:
            mwff = choose(mw9,mw11,f16(9,11))
        
        if mwee2 == mw14:
            mwff = choose(mw9,mw14,f16(9,14))      
        
        if mwee2 == mw15:
            mwff = choose(mw9,mw15,f16(9,15))
            
        
            
            
    if mwee1 == mw12:
        
        if mwee2 == mw2:
            mwff = choose(mw12,mw2,f16(12,2))
        
        if mwee2 == mw3:
            mwff = choose(mw12,mw3,f16(12,3))
        
        if mwee2 == mw6:
            mwff = choose(mw12,mw6,f16(12,6))      
        
        if mwee2 == mw7:
            mwff = choose(mw12,mw7,f16(12,7))
            
        if mwee2 == mw10:
            mwff = choose(mw12,mw10,f16(12,10))
        
        if mwee2 == mw11:
            mwff = choose(mw12,mw11,f16(12,11))
        
        if mwee2 == mw14:
            mwff = choose(mw12,mw14,f16(12,14))      
        
        if mwee2 == mw15:
            mwff = choose(mw12,mw15,f16(12,15))
            
        
            
            
    if mwee1 == mw13:
        
        if mwee2 == mw2:
            mwff = choose(mw13,mw2,f16(13,2))
        
        if mwee2 == mw3:
            mwff = choose(mw13,mw3,f16(13,3))
        
        if mwee2 == mw6:
            mwff = choose(mw13,mw6,f16(13,6))      
        
        if mwee2 == mw7:
            mwff = choose(mw13,mw7,f16(13,7))
            
        if mwee2 == mw10:
            mwff = choose(mw13,mw10,f16(13,10))
        
        if mwee2 == mw11:
            mwff = choose(mw13,mw11,f16(13,11))
        
        if mwee2 == mw14:
            mwff = choose(mw13,mw14,f16(13,14))      
        
        if mwee2 == mw15:
            mwff = choose(mw13,mw15,f16(13,15))
            
        
            
            
    if mwee1 == mw16:
        
        if mwee2 == mw2:
            mwff = choose(mw16,mw2,f16(16,2))
        
        if mwee2 == mw3:
            mwff = choose(mw16,mw3,f16(16,3))
        
        if mwee2 == mw6:
            mwff = choose(mw16,mw6,f16(16,6))      
        
        if mwee2 == mw7:
            mwff = choose(mw16,mw7,f16(16,7))
            
        if mwee2 == mw10:
            mwff = choose(mw16,mw10,f16(16,10))
        
        if mwee2 == mw11:
            mwff = choose(mw16,mw11,f16(16,11))
        
        if mwee2 == mw14:
            mwff = choose(mw16,mw14,f16(16,14))      
        
        if mwee2 == mw15:
            mwff = choose(mw16,mw15,f16(16,15))
            
        
            
            
            
            
            
            
            
            






    print('Final Four:')
    print('...')
    print(wff)
    print(eff)
    print(sff)
    print(mwff)
    print('...')
    



























#final four--------------------------------------------------------------------
































#west/east




    if wff == w1:
        
        if eff == e1:
            w_e = choose(w1,e1,f16(1,1))
        
        if eff == e2:
            w_e = choose(w1,e2,f16(1,2))
        
        if eff == e3:
            w_e = choose(w1,e3,f16(1,3))      
        
        if eff == e4:
            w_e = choose(w1,e4,f16(1,4))
            
        if eff == e5:
            w_e = choose(w1,e5,f16(1,5))
        
        if eff == e6:
            w_e = choose(w1,e6,f16(1,6))
        
        if eff == e7:
            w_e = choose(w1,e7,f16(1,7))      
        
        if eff == e8:
            w_e = choose(w1,e8,f16(1,8))
            
        if eff == e9:
            w_e = choose(w1,e9,f16(1,9))
        
        if eff == e10:
            w_e = choose(w1,e10,f16(1,10))
        
        if eff == e11:
            w_e = choose(w1,e11,f16(1,11))      
        
        if eff == e12:
            w_e = choose(w1,e12,f16(1,12))
            
        if eff == e13:
            w_e = choose(w1,e13,f16(1,13))
        
        if eff == e14:
            w_e = choose(w1,e14,f16(1,14))
        
        if eff == e15:
            w_e = choose(w1,e15,f16(1,15))      
        
        if eff == e16:
            w_e = choose(w1,e16,f16(1,16))
            
        
                    
            
    if wff == w2:
        
        if eff == e1:
            w_e = choose(w2,e1,f16(2,1))
        
        if eff == e2:
            w_e = choose(w2,e2,f16(2,2))
        
        if eff == e3:
            w_e = choose(w2,e3,f16(2,3))      
        
        if eff == e4:
            w_e = choose(w2,e4,f16(2,4))
            
        if eff == e5:
            w_e = choose(w2,e5,f16(2,5))
        
        if eff == e6:
            w_e = choose(w2,e6,f16(2,6))
        
        if eff == e7:
            w_e = choose(w2,e7,f16(2,7))      
        
        if eff == e8:
            w_e = choose(w2,e8,f16(2,8))
            
        if eff == e9:
            w_e = choose(w2,e9,f16(2,9))
        
        if eff == e10:
            w_e = choose(w2,e10,f16(2,10))
        
        if eff == e11:
            w_e = choose(w2,e11,f16(2,11))      
        
        if eff == e12:
            w_e = choose(w2,e12,f16(2,12))
            
        if eff == e13:
            w_e = choose(w2,e13,f16(2,13))
        
        if eff == e14:
            w_e = choose(w2,e14,f16(2,14))
        
        if eff == e15:
            w_e = choose(w2,e15,f16(2,15))      
        
        if eff == e16:
            w_e = choose(w2,e16,f16(2,16))
            
        
            
               
    if wff == w3:
        
        if eff == e1:
            w_e = choose(w3,e1,f16(3,1))
        
        if eff == e2:
            w_e = choose(w3,e2,f16(3,2))
        
        if eff == e3:
            w_e = choose(w3,e3,f16(3,3))      
        
        if eff == e4:
            w_e = choose(w3,e4,f16(3,4))
            
        if eff == e5:
            w_e = choose(w3,e5,f16(3,5))
        
        if eff == e6:
            w_e = choose(w3,e6,f16(3,6))
        
        if eff == e7:
            w_e = choose(w3,e7,f16(3,7))      
        
        if eff == e8:
            w_e = choose(w3,e8,f16(3,8))
            
        if eff == e9:
            w_e = choose(w3,e9,f16(3,9))
        
        if eff == e10:
            w_e = choose(w3,e10,f16(3,10))
        
        if eff == e11:
            w_e = choose(w3,e11,f16(3,11))      
        
        if eff == e12:
            w_e = choose(w3,e12,f16(3,12))
            
        if eff == e13:
            w_e = choose(w3,e13,f16(3,13))
        
        if eff == e14:
            w_e = choose(w3,e14,f16(3,14))
        
        if eff == e15:
            w_e = choose(w3,e15,f16(3,15))      
        
        if eff == e16:
            w_e = choose(w3,e16,f16(3,16))
            
        
            
            
    if wff == w4:
        
        if eff == e1:
            w_e = choose(w4,e1,f16(4,1))
        
        if eff == e2:
            w_e = choose(w4,e2,f16(4,2))
        
        if eff == e3:
            w_e = choose(w4,e3,f16(4,3))      
        
        if eff == e4:
            w_e = choose(w4,e4,f16(4,4))
            
        if eff == e5:
            w_e = choose(w4,e5,f16(4,5))
        
        if eff == e6:
            w_e = choose(w4,e6,f16(4,6))
        
        if eff == e7:
            w_e = choose(w4,e7,f16(4,7))      
        
        if eff == e8:
            w_e = choose(w4,e8,f16(4,8))
            
        if eff == e9:
            w_e = choose(w4,e9,f16(4,9))
        
        if eff == e10:
            w_e = choose(w4,e10,f16(4,10))
        
        if eff == e11:
            w_e = choose(w4,e11,f16(4,11))      
        
        if eff == e12:
            w_e = choose(w4,e12,f16(4,12))
            
        if eff == e13:
            w_e = choose(w4,e13,f16(4,13))
        
        if eff == e14:
            w_e = choose(w4,e14,f16(4,14))
        
        if eff == e15:
            w_e = choose(w4,e15,f16(4,15))      
        
        if eff == e16:
            w_e = choose(w4,e16,f16(4,16))
            
        
            
                       
    if wff == w5:
        
        if eff == e1:
            w_e = choose(w5,e1,f16(5,1))
        
        if eff == e2:
            w_e = choose(w5,e2,f16(5,2))
        
        if eff == e3:
            w_e = choose(w5,e3,f16(5,3))      
        
        if eff == e4:
            w_e = choose(w5,e4,f16(5,4))
            
        if eff == e5:
            w_e = choose(w5,e5,f16(5,5))
        
        if eff == e6:
            w_e = choose(w5,e6,f16(5,6))
        
        if eff == e7:
            w_e = choose(w5,e7,f16(5,7))      
        
        if eff == e8:
            w_e = choose(w5,e8,f16(5,8))
            
        if eff == e9:
            w_e = choose(w5,e9,f16(5,9))
        
        if eff == e10:
            w_e = choose(w5,e10,f16(5,10))
        
        if eff == e11:
            w_e = choose(w5,e11,f16(5,11))      
        
        if eff == e12:
            w_e = choose(w5,e12,f16(5,12))
            
        if eff == e13:
            w_e = choose(w5,e13,f16(5,13))
        
        if eff == e14:
            w_e = choose(w5,e14,f16(5,14))
        
        if eff == e15:
            w_e = choose(w5,e15,f16(5,15))      
        
        if eff == e16:
            w_e = choose(w5,e16,f16(5,16))
            
        
            
            
    if wff == w6:
        
        if eff == e1:
            w_e = choose(w6,e1,f16(6,1))
        
        if eff == e2:
            w_e = choose(w6,e2,f16(6,2))
        
        if eff == e3:
            w_e = choose(w6,e3,f16(6,3))      
        
        if eff == e4:
            w_e = choose(w6,e4,f16(6,4))
            
        if eff == e5:
            w_e = choose(w6,e5,f16(6,5))
        
        if eff == e6:
            w_e = choose(w6,e6,f16(6,6))
        
        if eff == e7:
            w_e = choose(w6,e7,f16(6,7))      
        
        if eff == e8:
            w_e = choose(w6,e8,f16(6,8))
            
        if eff == e9:
            w_e = choose(w6,e9,f16(6,9))
        
        if eff == e10:
            w_e = choose(w6,e10,f16(6,10))
        
        if eff == e11:
            w_e = choose(w6,e11,f16(6,11))      
        
        if eff == e12:
            w_e = choose(w6,e12,f16(6,12))
            
        if eff == e13:
            w_e = choose(w6,e13,f16(6,13))
        
        if eff == e14:
            w_e = choose(w6,e14,f16(6,14))
        
        if eff == e15:
            w_e = choose(w6,e15,f16(6,15))      
        
        if eff == e16:
            w_e = choose(w6,e16,f16(6,16))
            
        
                       
            
    if wff == w7:
        
        if eff == e1:
            w_e = choose(w7,e1,f16(7,1))
        
        if eff == e2:
            w_e = choose(w7,e2,f16(7,2))
        
        if eff == e3:
            w_e = choose(w7,e3,f16(7,3))      
        
        if eff == e4:
            w_e = choose(w7,e4,f16(7,4))
            
        if eff == e5:
            w_e = choose(w7,e5,f16(7,5))
        
        if eff == e6:
            w_e = choose(w7,e6,f16(7,6))
        
        if eff == e7:
            w_e = choose(w7,e7,f16(7,7))      
        
        if eff == e8:
            w_e = choose(w7,e8,f16(7,8))
            
        if eff == e9:
            w_e = choose(w7,e9,f16(7,9))
        
        if eff == e10:
            w_e = choose(w7,e10,f16(7,10))
        
        if eff == e11:
            w_e = choose(w7,e11,f16(7,11))      
        
        if eff == e12:
            w_e = choose(w7,e12,f16(7,12))
            
        if eff == e13:
            w_e = choose(w7,e13,f16(7,13))
        
        if eff == e14:
            w_e = choose(w7,e14,f16(7,14))
        
        if eff == e15:
            w_e = choose(w7,e15,f16(7,15))      
        
        if eff == e16:
            w_e = choose(w7,e16,f16(7,16))
            
        
            
                   
    if wff == w8:
        
        if eff == e1:
            w_e = choose(w8,e1,f16(8,1))
        
        if eff == e2:
            w_e = choose(w8,e2,f16(8,2))
        
        if eff == e3:
            w_e = choose(w8,e3,f16(8,3))      
        
        if eff == e4:
            w_e = choose(w8,e4,f16(8,4))
            
        if eff == e5:
            w_e = choose(w8,e5,f16(8,5))
        
        if eff == e6:
            w_e = choose(w8,e6,f16(8,6))
        
        if eff == e7:
            w_e = choose(w8,e7,f16(8,7))      
        
        if eff == e8:
            w_e = choose(w8,e8,f16(8,8))
            
        if eff == e9:
            w_e = choose(w8,e9,f16(8,9))
        
        if eff == e10:
            w_e = choose(w8,e10,f16(8,10))
        
        if eff == e11:
            w_e = choose(w8,e11,f16(8,11))      
        
        if eff == e12:
            w_e = choose(w8,e12,f16(8,12))
            
        if eff == e13:
            w_e = choose(w8,e13,f16(8,13))
        
        if eff == e14:
            w_e = choose(w8,e14,f16(8,14))
        
        if eff == e15:
            w_e = choose(w8,e15,f16(8,15))      
        
        if eff == e16:
            w_e = choose(w8,e16,f16(8,16))
            
        
            
            
            
    if wff == w9:
        
        if eff == e1:
            w_e = choose(w9,e1,f16(9,1))
        
        if eff == e2:
            w_e = choose(w9,e2,f16(9,2))
        
        if eff == e3:
            w_e = choose(w9,e3,f16(9,3))      
        
        if eff == e4:
            w_e = choose(w9,e4,f16(9,4))
            
        if eff == e5:
            w_e = choose(w9,e5,f16(9,5))
        
        if eff == e6:
            w_e = choose(w9,e6,f16(9,6))
        
        if eff == e7:
            w_e = choose(w9,e7,f16(9,7))      
        
        if eff == e8:
            w_e = choose(w9,e8,f16(9,8))
            
        if eff == e9:
            w_e = choose(w9,e9,f16(9,9))
        
        if eff == e10:
            w_e = choose(w9,e10,f16(9,10))
        
        if eff == e11:
            w_e = choose(w9,e11,f16(9,11))      
        
        if eff == e12:
            w_e = choose(w9,e12,f16(9,12))
            
        if eff == e13:
            w_e = choose(w9,e13,f16(9,13))
        
        if eff == e14:
            w_e = choose(w9,e14,f16(9,14))
        
        if eff == e15:
            w_e = choose(w9,e15,f16(9,15))      
        
        if eff == e16:
            w_e = choose(w9,e16,f16(9,16))
            
        
            
            
            
    if wff == w10:
        
        if eff == e1:
            w_e = choose(w10,e1,f16(10,1))
        
        if eff == e2:
            w_e = choose(w10,e2,f16(10,2))
        
        if eff == e3:
            w_e = choose(w10,e3,f16(10,3))      
        
        if eff == e4:
            w_e = choose(w10,e4,f16(10,4))
            
        if eff == e5:
            w_e = choose(w10,e5,f16(10,5))
        
        if eff == e6:
            w_e = choose(w10,e6,f16(10,6))
        
        if eff == e7:
            w_e = choose(w10,e7,f16(10,7))      
        
        if eff == e8:
            w_e = choose(w10,e8,f16(10,8))
            
        if eff == e9:
            w_e = choose(w10,e9,f16(10,9))
        
        if eff == e10:
            w_e = choose(w10,e10,f16(10,10))
        
        if eff == e11:
            w_e = choose(w10,e11,f16(10,11))      
        
        if eff == e12:
            w_e = choose(w10,e12,f16(10,12))
            
        if eff == e13:
            w_e = choose(w10,e13,f16(10,13))
        
        if eff == e14:
            w_e = choose(w10,e14,f16(10,14))
        
        if eff == e15:
            w_e = choose(w10,e15,f16(10,15))      
        
        if eff == e16:
            w_e = choose(w10,e16,f16(10,16))
            
        
                        
            
            
    if wff == w11:
        
        if eff == e1:
            w_e = choose(w11,e1,f16(11,1))
        
        if eff == e2:
            w_e = choose(w11,e2,f16(11,2))
        
        if eff == e3:
            w_e = choose(w11,e3,f16(11,3))      
        
        if eff == e4:
            w_e = choose(w11,e4,f16(11,4))
            
        if eff == e5:
            w_e = choose(w11,e5,f16(11,5))
        
        if eff == e6:
            w_e = choose(w11,e6,f16(11,6))
        
        if eff == e7:
            w_e = choose(w11,e7,f16(11,7))      
        
        if eff == e8:
            w_e = choose(w11,e8,f16(11,8))
            
        if eff == e9:
            w_e = choose(w11,e9,f16(11,9))
        
        if eff == e10:
            w_e = choose(w11,e10,f16(11,10))
        
        if eff == e11:
            w_e = choose(w11,e11,f16(11,11))      
        
        if eff == e12:
            w_e = choose(w11,e12,f16(11,12))
            
        if eff == e13:
            w_e = choose(w11,e13,f16(11,13))
        
        if eff == e14:
            w_e = choose(w11,e14,f16(11,14))
        
        if eff == e15:
            w_e = choose(w11,e15,f16(11,15))      
        
        if eff == e16:
            w_e = choose(w11,e16,f16(11,16))
            
        
            
            
            
    if wff == w12:
        
        if eff == e1:
            w_e = choose(w12,e1,f16(12,1))
        
        if eff == e2:
            w_e = choose(w12,e2,f16(12,2))
        
        if eff == e3:
            w_e = choose(w12,e3,f16(12,3))      
        
        if eff == e4:
            w_e = choose(w12,e4,f16(12,4))
            
        if eff == e5:
            w_e = choose(w12,e5,f16(12,5))
        
        if eff == e6:
            w_e = choose(w12,e6,f16(12,6))
        
        if eff == e7:
            w_e = choose(w12,e7,f16(12,7))      
        
        if eff == e8:
            w_e = choose(w12,e8,f16(12,8))
            
        if eff == e9:
            w_e = choose(w12,e9,f16(12,9))
        
        if eff == e10:
            w_e = choose(w12,e10,f16(12,10))
        
        if eff == e11:
            w_e = choose(w12,e11,f16(12,11))      
        
        if eff == e12:
            w_e = choose(w12,e12,f16(12,12))
            
        if eff == e13:
            w_e = choose(w12,e13,f16(12,13))
        
        if eff == e14:
            w_e = choose(w12,e14,f16(12,14))
        
        if eff == e15:
            w_e = choose(w12,e15,f16(12,15))      
        
        if eff == e16:
            w_e = choose(w12,e16,f16(12,16))
            
        
            
            
            
    if wff == w13:
        
        if eff == e1:
            w_e = choose(w13,e1,f16(13,1))
        
        if eff == e2:
            w_e = choose(w13,e2,f16(13,2))
        
        if eff == e3:
            w_e = choose(w13,e3,f16(13,3))      
        
        if eff == e4:
            w_e = choose(w13,e4,f16(13,4))
            
        if eff == e5:
            w_e = choose(w13,e5,f16(13,5))
        
        if eff == e6:
            w_e = choose(w13,e6,f16(13,6))
        
        if eff == e7:
            w_e = choose(w13,e7,f16(13,7))      
        
        if eff == e8:
            w_e = choose(w13,e8,f16(13,8))
            
        if eff == e9:
            w_e = choose(w13,e9,f16(13,9))
        
        if eff == e10:
            w_e = choose(w13,e10,f16(13,10))
        
        if eff == e11:
            w_e = choose(w13,e11,f16(13,11))      
        
        if eff == e12:
            w_e = choose(w13,e12,f16(13,12))
            
        if eff == e13:
            w_e = choose(w13,e13,f16(13,13))
        
        if eff == e14:
            w_e = choose(w13,e14,f16(13,14))
        
        if eff == e15:
            w_e = choose(w13,e15,f16(13,15))      
        
        if eff == e16:
            w_e = choose(w13,e16,f16(13,16))
            
        
            
            

    if wff == w14:
        
        if eff == e1:
            w_e = choose(w14,e1,f16(14,1))
        
        if eff == e2:
            w_e = choose(w14,e2,f16(14,2))
        
        if eff == e3:
            w_e = choose(w14,e3,f16(14,3))      
        
        if eff == e4:
            w_e = choose(w14,e4,f16(14,4))
            
        if eff == e5:
            w_e = choose(w14,e5,f16(14,5))
        
        if eff == e6:
            w_e = choose(w14,e6,f16(14,6))
        
        if eff == e7:
            w_e = choose(w14,e7,f16(14,7))      
        
        if eff == e8:
            w_e = choose(w14,e8,f16(14,8))
            
        if eff == e9:
            w_e = choose(w14,e9,f16(14,9))
        
        if eff == e10:
            w_e = choose(w14,e10,f16(14,10))
        
        if eff == e11:
            w_e = choose(w14,e12,f16(14,11))      
        
        if eff == e12:
            w_e = choose(w14,e12,f16(14,12))
            
        if eff == e13:
            w_e = choose(w14,e13,f16(14,13))
        
        if eff == e14:
            w_e = choose(w14,e14,f16(14,14))
        
        if eff == e15:
            w_e = choose(w14,e15,f16(14,15))      
        
        if eff == e16:
            w_e = choose(w14,e16,f16(14,16))
            
        
            
            
            
    if wff == w15:
        
        if eff == e1:
            w_e = choose(w15,e1,f16(15,1))
        
        if eff == e2:
            w_e = choose(w15,e2,f16(15,2))
        
        if eff == e3:
            w_e = choose(w15,e3,f16(15,3))      
        
        if eff == e4:
            w_e = choose(w15,e4,f16(15,4))
            
        if eff == e5:
            w_e = choose(w15,e5,f16(15,5))
        
        if eff == e6:
            w_e = choose(w15,e6,f16(15,6))
        
        if eff == e7:
            w_e = choose(w15,e7,f16(15,7))      
        
        if eff == e8:
            w_e = choose(w15,e8,f16(15,8))
            
        if eff == e9:
            w_e = choose(w15,e9,f16(15,9))
        
        if eff == e10:
            w_e = choose(w15,e10,f16(15,10))
        
        if eff == e11:
            w_e = choose(w15,e12,f16(15,11))      
        
        if eff == e12:
            w_e = choose(w15,e12,f16(15,12))
            
        if eff == e13:
            w_e = choose(w15,e13,f16(15,13))
        
        if eff == e14:
            w_e = choose(w15,e14,f16(15,14))
        
        if eff == e15:
            w_e = choose(w15,e15,f16(15,15))      
        
        if eff == e16:
            w_e = choose(w15,e16,f16(15,16))
            
        
            
            
            
    if wff == w16:
        
        if eff == e1:
            w_e = choose(w16,e1,f16(16,1))
        
        if eff == e2:
            w_e = choose(w16,e2,f16(16,2))
        
        if eff == e3:
            w_e = choose(w16,e3,f16(16,3))      
        
        if eff == e4:
            w_e = choose(w16,e4,f16(16,4))
            
        if eff == e5:
            w_e = choose(w16,e5,f16(16,5))
        
        if eff == e6:
            w_e = choose(w16,e6,f16(16,6))
        
        if eff == e7:
            w_e = choose(w16,e7,f16(16,7))      
        
        if eff == e8:
            w_e = choose(w16,e8,f16(16,8))
            
        if eff == e9:
            w_e = choose(w16,e9,f16(16,9))
        
        if eff == e10:
            w_e = choose(w16,e10,f16(16,10))
        
        if eff == e11:
            w_e = choose(w16,e12,f16(16,11))      
        
        if eff == e12:
            w_e = choose(w16,e12,f16(16,12))
            
        if eff == e13:
            w_e = choose(w16,e13,f16(16,13))
        
        if eff == e14:
            w_e = choose(w16,e14,f16(16,14))
        
        if eff == e15:
            w_e = choose(w16,e15,f16(16,15))      
        
        if eff == e16:
            w_e = choose(w16,e16,f16(16,16))
            
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            




#south/midwest




    if sff == s1:
        
        if mwff == mw1:
            s_mw = choose(s1,mw1,f16(1,1))
        
        if mwff == mw2:
            s_mw = choose(s1,mw2,f16(1,2))
        
        if mwff == mw3:
            s_mw = choose(s1,mw3,f16(1,3))      
        
        if mwff == mw4:
            s_mw = choose(s1,mw4,f16(1,4))
            
        if mwff == mw5:
            s_mw = choose(s1,mw5,f16(1,5))
        
        if mwff == mw6:
            s_mw = choose(s1,mw6,f16(1,6))
        
        if mwff == mw7:
            s_mw = choose(s1,mw7,f16(1,7))      
        
        if mwff == mw8:
            s_mw = choose(s1,mw8,f16(1,8))
            
        if mwff == mw9:
            s_mw = choose(s1,mw9,f16(1,9))
        
        if mwff == mw10:
            s_mw = choose(s1,mw10,f16(1,10))
        
        if mwff == mw11:
            s_mw = choose(s1,mw11,f16(1,11))      
        
        if mwff == mw12:
            s_mw = choose(s1,mw12,f16(1,12))
            
        if mwff == mw13:
            s_mw = choose(s1,mw13,f16(1,13))
        
        if mwff == mw14:
            s_mw = choose(s1,mw14,f16(1,14))
        
        if mwff == mw15:
            s_mw = choose(s1,mw15,f16(1,15))      
        
        if mwff == mw16:
            s_mw = choose(s1,mw16,f16(1,16))
            
        
            
            
            
    if sff == s2:
        
        if mwff == mw1:
            s_mw = choose(s2,mw1,f16(2,1))
        
        if mwff == mw2:
            s_mw = choose(s2,mw2,f16(2,2))
        
        if mwff == mw3:
            s_mw = choose(s2,mw3,f16(2,3))      
        
        if mwff == mw4:
            s_mw = choose(s2,mw4,f16(2,4))
            
        if mwff == mw5:
            s_mw = choose(s2,mw5,f16(2,5))
        
        if mwff == mw6:
            s_mw = choose(s2,mw6,f16(2,6))
        
        if mwff == mw7:
            s_mw = choose(s2,mw7,f16(2,7))      
        
        if mwff == mw8:
            s_mw = choose(s2,mw8,f16(2,8))
            
        if mwff == mw9:
            s_mw = choose(s2,mw9,f16(2,9))
        
        if mwff == mw10:
            s_mw = choose(s2,mw10,f16(2,10))
        
        if mwff == mw11:
            s_mw = choose(s2,mw11,f16(2,11))      
        
        if mwff == mw12:
            s_mw = choose(s2,mw12,f16(2,12))
            
        if mwff == mw13:
            s_mw = choose(s2,mw13,f16(2,13))
        
        if mwff == mw14:
            s_mw = choose(s2,mw14,f16(2,14))
        
        if mwff == mw15:
            s_mw = choose(s2,mw15,f16(2,15))      
        
        if mwff == mw16:
            s_mw = choose(s2,mw16,f16(2,16))
            
        
            
            
            
    if sff == s3:
        
        if mwff == mw1:
            s_mw = choose(s3,mw1,f16(3,1))
        
        if mwff == mw2:
            s_mw = choose(s3,mw2,f16(3,2))
        
        if mwff == mw3:
            s_mw = choose(s3,mw3,f16(3,3))      
        
        if mwff == mw4:
            s_mw = choose(s3,mw4,f16(3,4))
            
        if mwff == mw5:
            s_mw = choose(s3,mw5,f16(3,5))
        
        if mwff == mw6:
            s_mw = choose(s3,mw6,f16(3,6))
        
        if mwff == mw7:
            s_mw = choose(s3,mw7,f16(3,7))      
        
        if mwff == mw8:
            s_mw = choose(s3,mw8,f16(3,8))
            
        if mwff == mw9:
            s_mw = choose(s3,mw9,f16(3,9))
        
        if mwff == mw10:
            s_mw = choose(s3,mw10,f16(3,10))
        
        if mwff == mw11:
            s_mw = choose(s3,mw11,f16(3,11))      
        
        if mwff == mw12:
            s_mw = choose(s3,mw12,f16(3,12))
            
        if mwff == mw13:
            s_mw = choose(s3,mw13,f16(3,13))
        
        if mwff == mw14:
            s_mw = choose(s3,mw14,f16(3,14))
        
        if mwff == mw15:
            s_mw = choose(s3,mw15,f16(3,15))      
        
        if mwff == mw16:
            s_mw = choose(s3,mw16,f16(3,16))
            
        
            
            
    if sff == s4:
        
        if mwff == mw1:
            s_mw = choose(s4,mw1,f16(4,1))
        
        if mwff == mw2:
            s_mw = choose(s4,mw2,f16(4,2))
        
        if mwff == mw3:
            s_mw = choose(s4,mw3,f16(4,3))      
        
        if mwff == mw4:
            s_mw = choose(s4,mw4,f16(4,4))
            
        if mwff == mw5:
            s_mw = choose(s4,mw5,f16(4,5))
        
        if mwff == mw6:
            s_mw = choose(s4,mw6,f16(4,6))
        
        if mwff == mw7:
            s_mw = choose(s4,mw7,f16(4,7))      
        
        if mwff == mw8:
            s_mw = choose(s4,mw8,f16(4,8))
            
        if mwff == mw9:
            s_mw = choose(s4,mw9,f16(4,9))
        
        if mwff == mw10:
            s_mw = choose(s4,mw10,f16(4,10))
        
        if mwff == mw11:
            s_mw = choose(s4,mw11,f16(4,11))      
        
        if mwff == mw12:
            s_mw = choose(s4,mw12,f16(4,12))
            
        if mwff == mw13:
            s_mw = choose(s4,mw13,f16(4,13))
        
        if mwff == mw14:
            s_mw = choose(s4,mw14,f16(4,14))
        
        if mwff == mw15:
            s_mw = choose(s4,mw15,f16(4,15))      
        
        if mwff == mw16:
            s_mw = choose(s4,mw16,f16(4,16))
            
        
            
            
            
    if sff == s5:
        
        if mwff == mw1:
            s_mw = choose(s5,mw1,f16(5,1))
        
        if mwff == mw2:
            s_mw = choose(s5,mw2,f16(5,2))
        
        if mwff == mw3:
            s_mw = choose(s5,mw3,f16(5,3))      
        
        if mwff == mw4:
            s_mw = choose(s5,mw4,f16(5,4))
            
        if mwff == mw5:
            s_mw = choose(s5,mw5,f16(5,5))
        
        if mwff == mw6:
            s_mw = choose(s5,mw6,f16(5,6))
        
        if mwff == mw7:
            s_mw = choose(s5,mw7,f16(5,7))      
        
        if mwff == mw8:
            s_mw = choose(s5,mw8,f16(5,8))
            
        if mwff == mw9:
            s_mw = choose(s5,mw9,f16(5,9))
        
        if mwff == mw10:
            s_mw = choose(s5,mw10,f16(5,10))
        
        if mwff == mw11:
            s_mw = choose(s5,mw11,f16(5,11))      
        
        if mwff == mw12:
            s_mw = choose(s5,mw12,f16(5,12))
            
        if mwff == mw13:
            s_mw = choose(s5,mw13,f16(5,13))
        
        if mwff == mw14:
            s_mw = choose(s5,mw14,f16(5,14))
        
        if mwff == mw15:
            s_mw = choose(s5,mw15,f16(5,15))      
        
        if mwff == mw16:
            s_mw = choose(s5,mw16,f16(5,16))
            
        
            
            
            
            
    if sff == s6:
        
        if mwff == mw1:
            s_mw = choose(s6,mw1,f16(6,1))
        
        if mwff == mw2:
            s_mw = choose(s6,mw2,f16(6,2))
        
        if mwff == mw3:
            s_mw = choose(s6,mw3,f16(6,3))      
        
        if mwff == mw4:
            s_mw = choose(s6,mw4,f16(6,4))
            
        if mwff == mw5:
            s_mw = choose(s6,mw5,f16(6,5))
        
        if mwff == mw6:
            s_mw = choose(s6,mw6,f16(6,6))
        
        if mwff == mw7:
            s_mw = choose(s6,mw7,f16(6,7))      
        
        if mwff == mw8:
            s_mw = choose(s6,mw8,f16(6,8))
            
        if mwff == mw9:
            s_mw = choose(s6,mw9,f16(6,9))
        
        if mwff == mw10:
            s_mw = choose(s6,mw10,f16(6,10))
        
        if mwff == mw11:
            s_mw = choose(s6,mw11,f16(6,11))      
        
        if mwff == mw12:
            s_mw = choose(s6,mw12,f16(6,12))
            
        if mwff == mw13:
            s_mw = choose(s6,mw13,f16(6,13))
        
        if mwff == mw14:
            s_mw = choose(s6,mw14,f16(6,14))
        
        if mwff == mw15:
            s_mw = choose(s6,mw15,f16(6,15))      
        
        if mwff == mw16:
            s_mw = choose(s6,mw16,f16(6,16))
            
        
            
            
            
    if sff == s7:
        
        if mwff == mw1:
            s_mw = choose(s7,mw1,f16(7,1))
        
        if mwff == mw2:
            s_mw = choose(s7,mw2,f16(7,2))
        
        if mwff == mw3:
            s_mw = choose(s7,mw3,f16(7,3))      
        
        if mwff == mw4:
            s_mw = choose(s7,mw4,f16(7,4))
            
        if mwff == mw5:
            s_mw = choose(s7,mw5,f16(7,5))
        
        if mwff == mw6:
            s_mw = choose(s7,mw6,f16(7,6))
        
        if mwff == mw7:
            s_mw = choose(s7,mw7,f16(7,7))      
        
        if mwff == mw8:
            s_mw = choose(s7,mw8,f16(7,8))
            
        if mwff == mw9:
            s_mw = choose(s7,mw9,f16(7,9))
        
        if mwff == mw10:
            s_mw = choose(s7,mw10,f16(7,10))
        
        if mwff == mw11:
            s_mw = choose(s7,mw11,f16(7,11))      
        
        if mwff == mw12:
            s_mw = choose(s7,mw12,f16(7,12))
            
        if mwff == mw13:
            s_mw = choose(s7,mw13,f16(7,13))
        
        if mwff == mw14:
            s_mw = choose(s7,mw14,f16(7,14))
        
        if mwff == mw15:
            s_mw = choose(s7,mw15,f16(7,15))      
        
        if mwff == mw16:
            s_mw = choose(s7,mw16,f16(7,16))
            
        
            
            
            
    if sff == s8:
        
        if mwff == mw1:
            s_mw = choose(s8,mw1,f16(8,1))
        
        if mwff == mw2:
            s_mw = choose(s8,mw2,f16(8,2))
        
        if mwff == mw3:
            s_mw = choose(s8,mw3,f16(8,3))      
        
        if mwff == mw4:
            s_mw = choose(s8,mw4,f16(8,4))
            
        if mwff == mw5:
            s_mw = choose(s8,mw5,f16(8,5))
        
        if mwff == mw6:
            s_mw = choose(s8,mw6,f16(8,6))
        
        if mwff == mw7:
            s_mw = choose(s8,mw7,f16(8,7))      
        
        if mwff == mw8:
            s_mw = choose(s8,mw8,f16(8,8))
            
        if mwff == mw9:
            s_mw = choose(s8,mw9,f16(8,9))
        
        if mwff == mw10:
            s_mw = choose(s8,mw10,f16(8,10))
        
        if mwff == mw11:
            s_mw = choose(s8,mw11,f16(8,11))      
        
        if mwff == mw12:
            s_mw = choose(s8,mw12,f16(8,12))
            
        if mwff == mw13:
            s_mw = choose(s8,mw13,f16(8,13))
        
        if mwff == mw14:
            s_mw = choose(s8,mw14,f16(8,14))
        
        if mwff == mw15:
            s_mw = choose(s8,mw15,f16(8,15))      
        
        if mwff == mw16:
            s_mw = choose(s8,mw16,f16(8,16))
            
        
            
            
            
    if sff == s9:
        
        if mwff == mw1:
            s_mw = choose(s9,mw1,f16(9,1))
        
        if mwff == mw2:
            s_mw = choose(s9,mw2,f16(9,2))
        
        if mwff == mw3:
            s_mw = choose(s9,mw3,f16(9,3))      
        
        if mwff == mw4:
            s_mw = choose(s9,mw4,f16(9,4))
            
        if mwff == mw5:
            s_mw = choose(s9,mw5,f16(9,5))
        
        if mwff == mw6:
            s_mw = choose(s9,mw6,f16(9,6))
        
        if mwff == mw7:
            s_mw = choose(s9,mw7,f16(9,7))      
        
        if mwff == mw8:
            s_mw = choose(s9,mw8,f16(9,8))
            
        if mwff == mw9:
            s_mw = choose(s9,mw9,f16(9,9))
        
        if mwff == mw10:
            s_mw = choose(s9,mw10,f16(9,10))
        
        if mwff == mw11:
            s_mw = choose(s9,mw11,f16(9,11))      
        
        if mwff == mw12:
            s_mw = choose(s9,mw12,f16(9,12))
            
        if mwff == mw13:
            s_mw = choose(s9,mw13,f16(9,13))
        
        if mwff == mw14:
            s_mw = choose(s9,mw14,f16(9,14))
        
        if mwff == mw15:
            s_mw = choose(s9,mw15,f16(9,15))      
        
        if mwff == mw16:
            s_mw = choose(s9,mw16,f16(9,16))
            
        
            
            
            
    if sff == s10:
        
        if mwff == mw1:
            s_mw = choose(s10,mw1,f16(10,1))
        
        if mwff == mw2:
            s_mw = choose(s10,mw2,f16(10,2))
        
        if mwff == mw3:
            s_mw = choose(s10,mw3,f16(10,3))      
        
        if mwff == mw4:
            s_mw = choose(s10,mw4,f16(10,4))
            
        if mwff == mw5:
            s_mw = choose(s10,mw5,f16(10,5))
        
        if mwff == mw6:
            s_mw = choose(s10,mw6,f16(10,6))
        
        if mwff == mw7:
            s_mw = choose(s10,mw7,f16(10,7))      
        
        if mwff == mw8:
            s_mw = choose(s10,mw8,f16(10,8))
            
        if mwff == mw9:
            s_mw = choose(s10,mw9,f16(10,9))
        
        if mwff == mw10:
            s_mw = choose(s10,mw10,f16(10,10))
        
        if mwff == mw11:
            s_mw = choose(s10,mw11,f16(10,11))      
        
        if mwff == mw12:
            s_mw = choose(s10,mw12,f16(10,12))
            
        if mwff == mw13:
            s_mw = choose(s10,mw13,f16(10,13))
        
        if mwff == mw14:
            s_mw = choose(s10,mw14,f16(10,14))
        
        if mwff == mw15:
            s_mw = choose(s10,mw15,f16(10,15))      
        
        if mwff == mw16:
            s_mw = choose(s10,mw16,f16(10,16))
            
        
                        
            
            
    if sff == s11:
        
        if mwff == mw1:
            s_mw = choose(s11,mw1,f16(11,1))
        
        if mwff == mw2:
            s_mw = choose(s11,mw2,f16(11,2))
        
        if mwff == mw3:
            s_mw = choose(s11,mw3,f16(11,3))      
        
        if mwff == mw4:
            s_mw = choose(s11,mw4,f16(11,4))
            
        if mwff == mw5:
            s_mw = choose(s11,mw5,f16(11,5))
        
        if mwff == mw6:
            s_mw = choose(s11,mw6,f16(11,6))
        
        if mwff == mw7:
            s_mw = choose(s11,mw7,f16(11,7))      
        
        if mwff == mw8:
            s_mw = choose(s11,mw8,f16(11,8))
            
        if mwff == mw9:
            s_mw = choose(s11,mw9,f16(11,9))
        
        if mwff == mw10:
            s_mw = choose(s11,mw10,f16(11,10))
        
        if mwff == mw11:
            s_mw = choose(s11,mw11,f16(11,11))      
        
        if mwff == mw12:
            s_mw = choose(s11,mw12,f16(11,12))
            
        if mwff == mw13:
            s_mw = choose(s11,mw13,f16(11,13))
        
        if mwff == mw14:
            s_mw = choose(s11,mw14,f16(11,14))
        
        if mwff == mw15:
            s_mw = choose(s11,mw15,f16(11,15))      
        
        if mwff == mw16:
            s_mw = choose(s11,mw16,f16(11,16))
            
        
            
            
            
    if sff == s12:
        
        if mwff == mw1:
            s_mw = choose(s12,mw1,f16(12,1))
        
        if mwff == mw2:
            s_mw = choose(s12,mw2,f16(12,2))
        
        if mwff == mw3:
            s_mw = choose(s12,mw3,f16(12,3))      
        
        if mwff == mw4:
            s_mw = choose(s12,mw4,f16(12,4))
            
        if mwff == mw5:
            s_mw = choose(s12,mw5,f16(12,5))
        
        if mwff == mw6:
            s_mw = choose(s12,mw6,f16(12,6))
        
        if mwff == mw7:
            s_mw = choose(s12,mw7,f16(12,7))      
        
        if mwff == mw8:
            s_mw = choose(s12,mw8,f16(12,8))
            
        if mwff == mw9:
            s_mw = choose(s12,mw9,f16(12,9))
        
        if mwff == mw10:
            s_mw = choose(s12,mw10,f16(12,10))
        
        if mwff == mw11:
            s_mw = choose(s12,mw11,f16(12,11))      
        
        if mwff == mw12:
            s_mw = choose(s12,mw12,f16(12,12))
            
        if mwff == mw13:
            s_mw = choose(s12,mw13,f16(12,13))
        
        if mwff == mw14:
            s_mw = choose(s12,mw14,f16(12,14))
        
        if mwff == mw15:
            s_mw = choose(s12,mw15,f16(12,15))      
        
        if mwff == mw16:
            s_mw = choose(s12,mw16,f16(12,16))
            
        
            
            
            
    if sff == s13:
        
        if mwff == mw1:
            s_mw = choose(s13,mw1,f16(13,1))
        
        if mwff == mw2:
            s_mw = choose(s13,mw2,f16(13,2))
        
        if mwff == mw3:
            s_mw = choose(s13,mw3,f16(13,3))      
        
        if mwff == mw4:
            s_mw = choose(s13,mw4,f16(13,4))
            
        if mwff == mw5:
            s_mw = choose(s13,mw5,f16(13,5))
        
        if mwff == mw6:
            s_mw = choose(s13,mw6,f16(13,6))
        
        if mwff == mw7:
            s_mw = choose(s13,mw7,f16(13,7))      
        
        if mwff == mw8:
            s_mw = choose(s13,mw8,f16(13,8))
            
        if mwff == mw9:
            s_mw = choose(s13,mw9,f16(13,9))
        
        if mwff == mw10:
            s_mw = choose(s13,mw10,f16(13,10))
        
        if mwff == mw11:
            s_mw = choose(s13,mw11,f16(13,11))      
        
        if mwff == mw12:
            s_mw = choose(s13,mw12,f16(13,12))
            
        if mwff == mw13:
            s_mw = choose(s13,mw13,f16(13,13))
        
        if mwff == mw14:
            s_mw = choose(s13,mw14,f16(13,14))
        
        if mwff == mw15:
            s_mw = choose(s13,mw15,f16(13,15))      
        
        if mwff == mw16:
            s_mw = choose(s13,mw16,f16(13,16))
            
        
            
            

    if sff == s14:
        
        if mwff == mw1:
            s_mw = choose(s14,mw1,f16(14,1))
        
        if mwff == mw2:
            s_mw = choose(s14,mw2,f16(14,2))
        
        if mwff == mw3:
            s_mw = choose(s14,mw3,f16(14,3))      
        
        if mwff == mw4:
            s_mw = choose(s14,mw4,f16(14,4))
            
        if mwff == mw5:
            s_mw = choose(s14,mw5,f16(14,5))
        
        if mwff == mw6:
            s_mw = choose(s14,mw6,f16(14,6))
        
        if mwff == mw7:
            s_mw = choose(s14,mw7,f16(14,7))      
        
        if mwff == mw8:
            s_mw = choose(s14,mw8,f16(14,8))
            
        if mwff == mw9:
            s_mw = choose(s14,mw9,f16(14,9))
        
        if mwff == mw10:
            s_mw = choose(s14,mw10,f16(14,10))
        
        if mwff == mw11:
            s_mw = choose(s14,mw12,f16(14,11))      
        
        if mwff == mw12:
            s_mw = choose(s14,mw12,f16(14,12))
            
        if mwff == mw13:
            s_mw = choose(s14,mw13,f16(14,13))
        
        if mwff == mw14:
            s_mw = choose(s14,mw14,f16(14,14))
        
        if mwff == mw15:
            s_mw = choose(s14,mw15,f16(14,15))      
        
        if mwff == mw16:
            s_mw = choose(s14,mw16,f16(14,16))
            
        
            
            
            
    if sff == s15:
        
        if mwff == mw1:
            s_mw = choose(s15,mw1,f16(15,1))
        
        if mwff == mw2:
            s_mw = choose(s15,mw2,f16(15,2))
        
        if mwff == mw3:
            s_mw = choose(s15,mw3,f16(15,3))      
        
        if mwff == mw4:
            s_mw = choose(s15,mw4,f16(15,4))
            
        if mwff == mw5:
            s_mw = choose(s15,mw5,f16(15,5))
        
        if mwff == mw6:
            s_mw = choose(s15,mw6,f16(15,6))
        
        if mwff == mw7:
            s_mw = choose(s15,mw7,f16(15,7))      
        
        if mwff == mw8:
            s_mw = choose(s15,mw8,f16(15,8))
            
        if mwff == mw9:
            s_mw = choose(s15,mw9,f16(15,9))
        
        if mwff == mw10:
            s_mw = choose(s15,mw10,f16(15,10))
        
        if mwff == mw11:
            s_mw = choose(s15,mw12,f16(15,11))      
        
        if mwff == mw12:
            s_mw = choose(s15,mw12,f16(15,12))
            
        if mwff == mw13:
            s_mw = choose(s15,mw13,f16(15,13))
        
        if mwff == mw14:
            s_mw = choose(s15,mw14,f16(15,14))
        
        if mwff == mw15:
            s_mw = choose(s15,mw15,f16(15,15))      
        
        if mwff == mw16:
            s_mw = choose(s15,mw16,f16(15,16))
            
        
            
            
            
    if sff == s16:
        
        if mwff == mw1:
            s_mw = choose(s16,mw1,f16(16,1))
        
        if mwff == mw2:
            s_mw = choose(s16,mw2,f16(16,2))
        
        if mwff == mw3:
            s_mw = choose(s16,mw3,f16(16,3))      
        
        if mwff == mw4:
            s_mw = choose(s16,mw4,f16(16,4))
            
        if mwff == mw5:
            s_mw = choose(s16,mw5,f16(16,5))
        
        if mwff == mw6:
            s_mw = choose(s16,mw6,f16(16,6))
        
        if mwff == mw7:
            s_mw = choose(s16,mw7,f16(16,7))      
        
        if mwff == mw8:
            s_mw = choose(s16,mw8,f16(16,8))
            
        if mwff == mw9:
            s_mw = choose(s16,mw9,f16(16,9))
        
        if mwff == mw10:
            s_mw = choose(s16,mw10,f16(16,10))
        
        if mwff == mw11:
            s_mw = choose(s16,mw12,f16(16,11))      
        
        if mwff == mw12:
            s_mw = choose(s16,mw12,f16(16,12))
            
        if mwff == mw13:
            s_mw = choose(s16,mw13,f16(16,13))
        
        if mwff == mw14:
            s_mw = choose(s16,mw14,f16(16,14))
        
        if mwff == mw15:
            s_mw = choose(s16,mw15,f16(16,15))      
        
        if mwff == mw16:
            s_mw = choose(s16,mw16,f16(16,16))
            
        
            
            
            
    print('Championship game:')
    print('...')
    print(w_e)
    print(s_mw)
    print('...')
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
#championship game-------------------------------------------------------------
            
            
            
            

























    if w_e == w1:
        
        if s_mw == s1:
            c1 = choose(w1,s1,f16(1,1))
        
        if s_mw == s2:
            c1 = choose(w1,s2,f16(1,2))
        
        if s_mw == s3:
            c1 = choose(w1,s3,f16(1,3))      
        
        if s_mw == s4:
            c1 = choose(w1,s4,f16(1,4))
            
        if s_mw == s5:
            c1 = choose(w1,s5,f16(1,5))
        
        if s_mw == s6:
            c1 = choose(w1,s6,f16(1,6))
        
        if s_mw == s7:
            c1 = choose(w1,s7,f16(1,7))      
        
        if s_mw == s8:
            c1 = choose(w1,s8,f16(1,8))
            
        if s_mw == s9:
            c1 = choose(w1,s9,f16(1,9))
        
        if s_mw == s10:
            c1 = choose(w1,s10,f16(1,10))
        
        if s_mw == s11:
            c1 = choose(w1,s11,f16(1,11))      
        
        if s_mw == s12:
            c1 = choose(w1,s12,f16(1,12))
            
        if s_mw == s13:
            c1 = choose(w1,s13,f16(1,13))
        
        if s_mw == s14:
            c1 = choose(w1,s14,f16(1,14))
        
        if s_mw == s15:
            c1 = choose(w1,s15,f16(1,15))      
        
        if s_mw == s16:
            c1 = choose(w1,s16,f16(1,16))
            
        if s_mw == mw1:
            c1 = choose(w1,mw1,f16(1,1))
        
        if s_mw == mw2:
            c1 = choose(w1,mw2,f16(1,2))
        
        if s_mw == mw3:
            c1 = choose(w1,mw3,f16(1,3))      
        
        if s_mw == mw4:
            c1 = choose(w1,mw4,f16(1,4))
            
        if s_mw == mw5:
            c1 = choose(w1,mw5,f16(1,5))
        
        if s_mw == mw6:
            c1 = choose(w1,mw6,f16(1,6))
        
        if s_mw == mw7:
            c1 = choose(w1,mw7,f16(1,7))      
        
        if s_mw == mw8:
            c1 = choose(w1,mw8,f16(1,8))
            
        if s_mw == mw9:
            c1 = choose(w1,mw9,f16(1,9))
        
        if s_mw == mw10:
            c1 = choose(w1,mw10,f16(1,10))
        
        if s_mw == mw11:
            c1 = choose(w1,mw11,f16(1,11))      
        
        if s_mw == mw12:
            c1 = choose(w1,mw12,f16(1,12))
            
        if s_mw == mw13:
            c1 = choose(w1,mw13,f16(1,13))
        
        if s_mw == mw14:
            c1 = choose(w1,mw14,f16(1,14))
        
        if s_mw == mw15:
            c1 = choose(w1,mw15,f16(1,15))      
        
        if s_mw == mw16:
            c1 = choose(w1,mw16,f16(1,16))
            
        
                 
            
            
    if w_e == w2:
        
        if s_mw == s1:
            c1 = choose(w2,s1,f16(2,1))
        
        if s_mw == s2:
            c1 = choose(w2,s2,f16(2,2))
        
        if s_mw == s3:
            c1 = choose(w2,s3,f16(2,3))      
        
        if s_mw == s4:
            c1 = choose(w2,s4,f16(2,4))
            
        if s_mw == s5:
            c1 = choose(w2,s5,f16(2,5))
        
        if s_mw == s6:
            c1 = choose(w2,s6,f16(2,6))
        
        if s_mw == s7:
            c1 = choose(w2,s7,f16(2,7))      
        
        if s_mw == s8:
            c1 = choose(w2,s8,f16(2,8))
            
        if s_mw == s9:
            c1 = choose(w2,s9,f16(2,9))
        
        if s_mw == s10:
            c1 = choose(w2,s10,f16(2,10))
        
        if s_mw == s11:
            c1 = choose(w2,s11,f16(2,11))      
        
        if s_mw == s12:
            c1 = choose(w2,s12,f16(2,12))
            
        if s_mw == s13:
            c1 = choose(w2,s13,f16(2,13))
        
        if s_mw == s14:
            c1 = choose(w2,s14,f16(2,14))
        
        if s_mw == s15:
            c1 = choose(w2,s15,f16(2,15))      
        
        if s_mw == s16:
            c1 = choose(w2,s16,f16(2,16))
            
        if s_mw == mw1:
            c1 = choose(w2,mw1,f16(2,1))
        
        if s_mw == mw2:
            c1 = choose(w2,mw2,f16(2,2))
        
        if s_mw == mw3:
            c1 = choose(w2,mw3,f16(2,3))      
        
        if s_mw == mw4:
            c1 = choose(w2,mw4,f16(2,4))
            
        if s_mw == mw5:
            c1 = choose(w2,mw5,f16(2,5))
        
        if s_mw == mw6:
            c1 = choose(w2,mw6,f16(2,6))
        
        if s_mw == mw7:
            c1 = choose(w2,mw7,f16(2,7))      
        
        if s_mw == mw8:
            c1 = choose(w2,mw8,f16(2,8))
            
        if s_mw == mw9:
            c1 = choose(w2,mw9,f16(2,9))
        
        if s_mw == mw10:
            c1 = choose(w2,mw10,f16(2,10))
        
        if s_mw == mw11:
            c1 = choose(w2,mw11,f16(2,11))      
        
        if s_mw == mw12:
            c1 = choose(w2,mw12,f16(2,12))
            
        if s_mw == mw13:
            c1 = choose(w2,mw13,f16(2,13))
        
        if s_mw == mw14:
            c1 = choose(w2,mw14,f16(2,14))
        
        if s_mw == mw15:
            c1 = choose(w2,mw15,f16(2,15))      
        
        if s_mw == mw16:
            c1 = choose(w2,mw16,f16(2,16))
            
        
                 
            
            
    if w_e == w3:
        
        if s_mw == s1:
            c1 = choose(w3,s1,f16(3,1))
        
        if s_mw == s2:
            c1 = choose(w3,s2,f16(3,2))
        
        if s_mw == s3:
            c1 = choose(w3,s3,f16(3,3))      
        
        if s_mw == s4:
            c1 = choose(w3,s4,f16(3,4))
            
        if s_mw == s5:
            c1 = choose(w3,s5,f16(3,5))
        
        if s_mw == s6:
            c1 = choose(w3,s6,f16(3,6))
        
        if s_mw == s7:
            c1 = choose(w3,s7,f16(3,7))      
        
        if s_mw == s8:
            c1 = choose(w3,s8,f16(3,8))
            
        if s_mw == s9:
            c1 = choose(w3,s9,f16(3,9))
        
        if s_mw == s10:
            c1 = choose(w3,s10,f16(3,10))
        
        if s_mw == s11:
            c1 = choose(w3,s11,f16(3,11))      
        
        if s_mw == s12:
            c1 = choose(w3,s12,f16(3,12))
            
        if s_mw == s13:
            c1 = choose(w3,s13,f16(3,13))
        
        if s_mw == s14:
            c1 = choose(w3,s14,f16(3,14))
        
        if s_mw == s15:
            c1 = choose(w3,s15,f16(3,15))      
        
        if s_mw == s16:
            c1 = choose(w3,s16,f16(3,16))
            
        if s_mw == mw1:
            c1 = choose(w3,mw1,f16(3,1))
        
        if s_mw == mw2:
            c1 = choose(w3,mw2,f16(3,2))
        
        if s_mw == mw3:
            c1 = choose(w3,mw3,f16(3,3))      
        
        if s_mw == mw4:
            c1 = choose(w3,mw4,f16(3,4))
            
        if s_mw == mw5:
            c1 = choose(w3,mw5,f16(3,5))
        
        if s_mw == mw6:
            c1 = choose(w3,mw6,f16(3,6))
        
        if s_mw == mw7:
            c1 = choose(w3,mw7,f16(3,7))      
        
        if s_mw == mw8:
            c1 = choose(w3,mw8,f16(3,8))
            
        if s_mw == mw9:
            c1 = choose(w3,mw9,f16(3,9))
        
        if s_mw == mw10:
            c1 = choose(w3,mw10,f16(3,10))
        
        if s_mw == mw11:
            c1 = choose(w3,mw11,f16(3,11))      
        
        if s_mw == mw12:
            c1 = choose(w3,mw12,f16(3,12))
            
        if s_mw == mw13:
            c1 = choose(w3,mw13,f16(3,13))
        
        if s_mw == mw14:
            c1 = choose(w3,mw14,f16(3,14))
        
        if s_mw == mw15:
            c1 = choose(w3,mw15,f16(3,15))      
        
        if s_mw == mw16:
            c1 = choose(w3,mw16,f16(3,16))
            
        
                 
            
    if w_e == w4:
        
        if s_mw == s1:
            c1 = choose(w4,s1,f16(4,1))
        
        if s_mw == s2:
            c1 = choose(w4,s2,f16(4,2))
        
        if s_mw == s3:
            c1 = choose(w4,s3,f16(4,3))      
        
        if s_mw == s4:
            c1 = choose(w4,s4,f16(4,4))
            
        if s_mw == s5:
            c1 = choose(w4,s5,f16(4,5))
        
        if s_mw == s6:
            c1 = choose(w4,s6,f16(4,6))
        
        if s_mw == s7:
            c1 = choose(w4,s7,f16(4,7))      
        
        if s_mw == s8:
            c1 = choose(w4,s8,f16(4,8))
            
        if s_mw == s9:
            c1 = choose(w4,s9,f16(4,9))
        
        if s_mw == s10:
            c1 = choose(w4,s10,f16(4,10))
        
        if s_mw == s11:
            c1 = choose(w4,s11,f16(4,11))      
        
        if s_mw == s12:
            c1 = choose(w4,s12,f16(4,12))
            
        if s_mw == s13:
            c1 = choose(w4,s13,f16(4,13))
        
        if s_mw == s14:
            c1 = choose(w4,s14,f16(4,14))
        
        if s_mw == s15:
            c1 = choose(w4,s15,f16(4,15))      
        
        if s_mw == s16:
            c1 = choose(w4,s16,f16(4,16))
            
        if s_mw == mw1:
            c1 = choose(w4,mw1,f16(4,1))
        
        if s_mw == mw2:
            c1 = choose(w4,mw2,f16(4,2))
        
        if s_mw == mw3:
            c1 = choose(w4,mw3,f16(4,3))      
        
        if s_mw == mw4:
            c1 = choose(w4,mw4,f16(4,4))
            
        if s_mw == mw5:
            c1 = choose(w4,mw5,f16(4,5))
        
        if s_mw == mw6:
            c1 = choose(w4,mw6,f16(4,6))
        
        if s_mw == mw7:
            c1 = choose(w4,mw7,f16(4,7))      
        
        if s_mw == mw8:
            c1 = choose(w4,mw8,f16(4,8))
            
        if s_mw == mw9:
            c1 = choose(w4,mw9,f16(4,9))
        
        if s_mw == mw10:
            c1 = choose(w4,mw10,f16(4,10))
        
        if s_mw == mw11:
            c1 = choose(w4,mw11,f16(4,11))      
        
        if s_mw == mw12:
            c1 = choose(w4,mw12,f16(4,12))
            
        if s_mw == mw13:
            c1 = choose(w4,mw13,f16(4,13))
        
        if s_mw == mw14:
            c1 = choose(w4,mw14,f16(4,14))
        
        if s_mw == mw15:
            c1 = choose(w4,mw15,f16(4,15))      
        
        if s_mw == mw16:
            c1 = choose(w4,mw16,f16(4,16))
            
        
                 
            
            
    if w_e == w5:
        
        if s_mw == s1:
            c1 = choose(w5,s1,f16(5,1))
        
        if s_mw == s2:
            c1 = choose(w5,s2,f16(5,2))
        
        if s_mw == s3:
            c1 = choose(w5,s3,f16(5,3))      
        
        if s_mw == s4:
            c1 = choose(w5,s4,f16(5,4))
            
        if s_mw == s5:
            c1 = choose(w5,s5,f16(5,5))
        
        if s_mw == s6:
            c1 = choose(w5,s6,f16(5,6))
        
        if s_mw == s7:
            c1 = choose(w5,s7,f16(5,7))      
        
        if s_mw == s8:
            c1 = choose(w5,s8,f16(5,8))
            
        if s_mw == s9:
            c1 = choose(w5,s9,f16(5,9))
        
        if s_mw == s10:
            c1 = choose(w5,s10,f16(5,10))
        
        if s_mw == s11:
            c1 = choose(w5,s11,f16(5,11))      
        
        if s_mw == s12:
            c1 = choose(w5,s12,f16(5,12))
            
        if s_mw == s13:
            c1 = choose(w5,s13,f16(5,13))
        
        if s_mw == s14:
            c1 = choose(w5,s14,f16(5,14))
        
        if s_mw == s15:
            c1 = choose(w5,s15,f16(5,15))      
        
        if s_mw == s16:
            c1 = choose(w5,s16,f16(5,16))
            
        if s_mw == mw1:
            c1 = choose(w5,mw1,f16(5,1))
        
        if s_mw == mw2:
            c1 = choose(w5,mw2,f16(5,2))
        
        if s_mw == mw3:
            c1 = choose(w5,mw3,f16(5,3))      
        
        if s_mw == mw4:
            c1 = choose(w5,mw4,f16(5,4))
            
        if s_mw == mw5:
            c1 = choose(w5,mw5,f16(5,5))
        
        if s_mw == mw6:
            c1 = choose(w5,mw6,f16(5,6))
        
        if s_mw == mw7:
            c1 = choose(w5,mw7,f16(5,7))      
        
        if s_mw == mw8:
            c1 = choose(w5,mw8,f16(5,8))
            
        if s_mw == mw9:
            c1 = choose(w5,mw9,f16(5,9))
        
        if s_mw == mw10:
            c1 = choose(w5,mw10,f16(5,10))
        
        if s_mw == mw11:
            c1 = choose(w5,mw11,f16(5,11))      
        
        if s_mw == mw12:
            c1 = choose(w5,mw12,f16(5,12))
            
        if s_mw == mw13:
            c1 = choose(w5,mw13,f16(5,13))
        
        if s_mw == mw14:
            c1 = choose(w5,mw14,f16(5,14))
        
        if s_mw == mw15:
            c1 = choose(w5,mw15,f16(5,15))      
        
        if s_mw == mw16:
            c1 = choose(w5,mw16,f16(5,16))
            
        
                 
            
            
    if w_e == w6:
        
        if s_mw == s1:
            c1 = choose(w6,s1,f16(6,1))
        
        if s_mw == s2:
            c1 = choose(w6,s2,f16(6,2))
        
        if s_mw == s3:
            c1 = choose(w6,s3,f16(6,3))      
        
        if s_mw == s4:
            c1 = choose(w6,s4,f16(6,4))
            
        if s_mw == s5:
            c1 = choose(w6,s5,f16(6,5))
        
        if s_mw == s6:
            c1 = choose(w6,s6,f16(6,6))
        
        if s_mw == s7:
            c1 = choose(w6,s7,f16(6,7))      
        
        if s_mw == s8:
            c1 = choose(w6,s8,f16(6,8))
            
        if s_mw == s9:
            c1 = choose(w6,s9,f16(6,9))
        
        if s_mw == s10:
            c1 = choose(w6,s10,f16(6,10))
        
        if s_mw == s11:
            c1 = choose(w6,s11,f16(6,11))      
        
        if s_mw == s12:
            c1 = choose(w6,s12,f16(6,12))
            
        if s_mw == s13:
            c1 = choose(w6,s13,f16(6,13))
        
        if s_mw == s14:
            c1 = choose(w6,s14,f16(6,14))
        
        if s_mw == s15:
            c1 = choose(w6,s15,f16(6,15))      
        
        if s_mw == s16:
            c1 = choose(w6,s16,f16(6,16))
            
        if s_mw == mw1:
            c1 = choose(w6,mw1,f16(6,1))
        
        if s_mw == mw2:
            c1 = choose(w6,mw2,f16(6,2))
        
        if s_mw == mw3:
            c1 = choose(w6,mw3,f16(6,3))      
        
        if s_mw == mw4:
            c1 = choose(w6,mw4,f16(6,4))
            
        if s_mw == mw5:
            c1 = choose(w6,mw5,f16(6,5))
        
        if s_mw == mw6:
            c1 = choose(w6,mw6,f16(6,6))
        
        if s_mw == mw7:
            c1 = choose(w6,mw7,f16(6,7))      
        
        if s_mw == mw8:
            c1 = choose(w6,mw8,f16(6,8))
            
        if s_mw == mw9:
            c1 = choose(w6,mw9,f16(6,9))
        
        if s_mw == mw10:
            c1 = choose(w6,mw10,f16(6,10))
        
        if s_mw == mw11:
            c1 = choose(w6,mw11,f16(6,11))      
        
        if s_mw == mw12:
            c1 = choose(w6,mw12,f16(6,12))
            
        if s_mw == mw13:
            c1 = choose(w6,mw13,f16(6,13))
        
        if s_mw == mw14:
            c1 = choose(w6,mw14,f16(6,14))
        
        if s_mw == mw15:
            c1 = choose(w6,mw15,f16(6,15))      
        
        if s_mw == mw16:
            c1 = choose(w6,mw16,f16(6,16))
            
        
                 
            
            
    if w_e == w7:
        
        if s_mw == s1:
            c1 = choose(w7,s1,f16(7,1))
        
        if s_mw == s2:
            c1 = choose(w7,s2,f16(7,2))
        
        if s_mw == s3:
            c1 = choose(w7,s3,f16(7,3))      
        
        if s_mw == s4:
            c1 = choose(w7,s4,f16(7,4))
            
        if s_mw == s5:
            c1 = choose(w7,s5,f16(7,5))
        
        if s_mw == s6:
            c1 = choose(w7,s6,f16(7,6))
        
        if s_mw == s7:
            c1 = choose(w7,s7,f16(7,7))      
        
        if s_mw == s8:
            c1 = choose(w7,s8,f16(7,8))
            
        if s_mw == s9:
            c1 = choose(w7,s9,f16(7,9))
        
        if s_mw == s10:
            c1 = choose(w7,s10,f16(7,10))
        
        if s_mw == s11:
            c1 = choose(w7,s11,f16(7,11))      
        
        if s_mw == s12:
            c1 = choose(w7,s12,f16(7,12))
            
        if s_mw == s13:
            c1 = choose(w7,s13,f16(7,13))
        
        if s_mw == s14:
            c1 = choose(w7,s14,f16(7,14))
        
        if s_mw == s15:
            c1 = choose(w7,s15,f16(7,15))      
        
        if s_mw == s16:
            c1 = choose(w7,s16,f16(7,16))
            
        if s_mw == mw1:
            c1 = choose(w7,mw1,f16(7,1))
        
        if s_mw == mw2:
            c1 = choose(w7,mw2,f16(7,2))
        
        if s_mw == mw3:
            c1 = choose(w7,mw3,f16(7,3))      
        
        if s_mw == mw4:
            c1 = choose(w7,mw4,f16(7,4))
            
        if s_mw == mw5:
            c1 = choose(w7,mw5,f16(7,5))
        
        if s_mw == mw6:
            c1 = choose(w7,mw6,f16(7,6))
        
        if s_mw == mw7:
            c1 = choose(w7,mw7,f16(7,7))      
        
        if s_mw == mw8:
            c1 = choose(w7,mw8,f16(7,8))
            
        if s_mw == mw9:
            c1 = choose(w7,mw9,f16(7,9))
        
        if s_mw == mw10:
            c1 = choose(w7,mw10,f16(7,10))
        
        if s_mw == mw11:
            c1 = choose(w7,mw11,f16(7,11))      
        
        if s_mw == mw12:
            c1 = choose(w7,mw12,f16(7,12))
            
        if s_mw == mw13:
            c1 = choose(w7,mw13,f16(7,13))
        
        if s_mw == mw14:
            c1 = choose(w7,mw14,f16(7,14))
        
        if s_mw == mw15:
            c1 = choose(w7,mw15,f16(7,15))      
        
        if s_mw == mw16:
            c1 = choose(w7,mw16,f16(7,16))
            
        
                 
            
            
    if w_e == w8:
        
        if s_mw == s1:
            c1 = choose(w_e,s1,f16(8,1))
        
        if s_mw == s2:
            c1 = choose(w_e,s2,f16(8,2))
        
        if s_mw == s3:
            c1 = choose(w_e,s3,f16(8,3))      
        
        if s_mw == s4:
            c1 = choose(w_e,s4,f16(8,4))
            
        if s_mw == s5:
            c1 = choose(w_e,s5,f16(8,5))
        
        if s_mw == s6:
            c1 = choose(w_e,s6,f16(8,6))
        
        if s_mw == s7:
            c1 = choose(w_e,s7,f16(8,7))      
        
        if s_mw == s8:
            c1 = choose(w_e,s8,f16(8,8))
            
        if s_mw == s9:
            c1 = choose(w_e,s9,f16(8,9))
        
        if s_mw == s10:
            c1 = choose(w_e,s10,f16(8,10))
        
        if s_mw == s11:
            c1 = choose(w_e,s11,f16(8,11))      
        
        if s_mw == s12:
            c1 = choose(w_e,s12,f16(8,12))
            
        if s_mw == s13:
            c1 = choose(w_e,s13,f16(8,13))
        
        if s_mw == s14:
            c1 = choose(w_e,s14,f16(8,14))
        
        if s_mw == s15:
            c1 = choose(w_e,s15,f16(8,15))      
        
        if s_mw == s16:
            c1 = choose(w_e,s16,f16(8,16))
            
        if s_mw == mw1:
            c1 = choose(w_e,mw1,f16(8,1))
        
        if s_mw == mw2:
            c1 = choose(w_e,mw2,f16(8,2))
        
        if s_mw == mw3:
            c1 = choose(w_e,mw3,f16(8,3))      
        
        if s_mw == mw4:
            c1 = choose(w_e,mw4,f16(8,4))
            
        if s_mw == mw5:
            c1 = choose(w_e,mw5,f16(8,5))
        
        if s_mw == mw6:
            c1 = choose(w_e,mw6,f16(8,6))
        
        if s_mw == mw7:
            c1 = choose(w_e,mw7,f16(8,7))      
        
        if s_mw == mw8:
            c1 = choose(w_e,mw8,f16(8,8))
            
        if s_mw == mw9:
            c1 = choose(w_e,mw9,f16(8,9))
        
        if s_mw == mw10:
            c1 = choose(w_e,mw10,f16(8,10))
        
        if s_mw == mw11:
            c1 = choose(w_e,mw11,f16(8,11))      
        
        if s_mw == mw12:
            c1 = choose(w_e,mw12,f16(8,12))
            
        if s_mw == mw13:
            c1 = choose(w_e,mw13,f16(8,13))
        
        if s_mw == mw14:
            c1 = choose(w_e,mw14,f16(8,14))
        
        if s_mw == mw15:
            c1 = choose(w_e,mw15,f16(8,15))      
        
        if s_mw == mw16:
            c1 = choose(w_e,mw16,f16(8,16))
            
        
                 
            
            
    if w_e == w9:
        
        if s_mw == s1:
            c1 = choose(w_e,s1,f16(9,1))
        
        if s_mw == s2:
            c1 = choose(w_e,s2,f16(9,2))
        
        if s_mw == s3:
            c1 = choose(w_e,s3,f16(9,3))      
        
        if s_mw == s4:
            c1 = choose(w_e,s4,f16(9,4))
            
        if s_mw == s5:
            c1 = choose(w_e,s5,f16(9,5))
        
        if s_mw == s6:
            c1 = choose(w_e,s6,f16(9,6))
        
        if s_mw == s7:
            c1 = choose(w_e,s7,f16(9,7))      
        
        if s_mw == s8:
            c1 = choose(w_e,s8,f16(9,8))
            
        if s_mw == s9:
            c1 = choose(w_e,s9,f16(9,9))
        
        if s_mw == s10:
            c1 = choose(w_e,s10,f16(9,10))
        
        if s_mw == s11:
            c1 = choose(w_e,s11,f16(9,11))      
        
        if s_mw == s12:
            c1 = choose(w_e,s12,f16(9,12))
            
        if s_mw == s13:
            c1 = choose(w_e,s13,f16(9,13))
        
        if s_mw == s14:
            c1 = choose(w_e,s14,f16(9,14))
        
        if s_mw == s15:
            c1 = choose(w_e,s15,f16(9,15))      
        
        if s_mw == s16:
            c1 = choose(w_e,s16,f16(9,16))
            
        if s_mw == mw1:
            c1 = choose(w_e,mw1,f16(9,1))
        
        if s_mw == mw2:
            c1 = choose(w_e,mw2,f16(9,2))
        
        if s_mw == mw3:
            c1 = choose(w_e,mw3,f16(9,3))      
        
        if s_mw == mw4:
            c1 = choose(w_e,mw4,f16(9,4))
            
        if s_mw == mw5:
            c1 = choose(w_e,mw5,f16(9,5))
        
        if s_mw == mw6:
            c1 = choose(w_e,mw6,f16(9,6))
        
        if s_mw == mw7:
            c1 = choose(w_e,mw7,f16(9,7))      
        
        if s_mw == mw8:
            c1 = choose(w_e,mw8,f16(9,8))
            
        if s_mw == mw9:
            c1 = choose(w_e,mw9,f16(9,9))
        
        if s_mw == mw10:
            c1 = choose(w_e,mw10,f16(9,10))
        
        if s_mw == mw11:
            c1 = choose(w_e,mw11,f16(9,11))      
        
        if s_mw == mw12:
            c1 = choose(w_e,mw12,f16(9,12))
            
        if s_mw == mw13:
            c1 = choose(w_e,mw13,f16(9,13))
        
        if s_mw == mw14:
            c1 = choose(w_e,mw14,f16(9,14))
        
        if s_mw == mw15:
            c1 = choose(w_e,mw15,f16(9,15))      
        
        if s_mw == mw16:
            c1 = choose(w_e,mw16,f16(9,16))
            
        
                 
            
            
    if w_e == w10:
        
        if s_mw == s1:
            c1 = choose(w_e,s1,f16(10,1))
        
        if s_mw == s2:
            c1 = choose(w_e,s2,f16(10,2))
        
        if s_mw == s3:
            c1 = choose(w_e,s3,f16(10,3))      
        
        if s_mw == s4:
            c1 = choose(w_e,s4,f16(10,4))
            
        if s_mw == s5:
            c1 = choose(w_e,s5,f16(10,5))
        
        if s_mw == s6:
            c1 = choose(w_e,s6,f16(10,6))
        
        if s_mw == s7:
            c1 = choose(w_e,s7,f16(10,7))      
        
        if s_mw == s8:
            c1 = choose(w_e,s8,f16(10,8))
            
        if s_mw == s9:
            c1 = choose(w_e,s9,f16(10,9))
        
        if s_mw == s10:
            c1 = choose(w_e,s10,f16(10,10))
        
        if s_mw == s11:
            c1 = choose(w_e,s11,f16(10,11))      
        
        if s_mw == s12:
            c1 = choose(w_e,s12,f16(10,12))
            
        if s_mw == s13:
            c1 = choose(w_e,s13,f16(10,13))
        
        if s_mw == s14:
            c1 = choose(w_e,s14,f16(10,14))
        
        if s_mw == s15:
            c1 = choose(w_e,s15,f16(10,15))      
        
        if s_mw == s16:
            c1 = choose(w_e,s16,f16(10,16))
            
        if s_mw == mw1:
            c1 = choose(w_e,mw1,f16(10,1))
        
        if s_mw == mw2:
            c1 = choose(w_e,mw2,f16(10,2))
        
        if s_mw == mw3:
            c1 = choose(w_e,mw3,f16(10,3))      
        
        if s_mw == mw4:
            c1 = choose(w_e,mw4,f16(10,4))
            
        if s_mw == mw5:
            c1 = choose(w_e,mw5,f16(10,5))
        
        if s_mw == mw6:
            c1 = choose(w_e,mw6,f16(10,6))
        
        if s_mw == mw7:
            c1 = choose(w_e,mw7,f16(10,7))      
        
        if s_mw == mw8:
            c1 = choose(w_e,mw8,f16(10,8))
            
        if s_mw == mw9:
            c1 = choose(w_e,mw9,f16(10,9))
        
        if s_mw == mw10:
            c1 = choose(w_e,mw10,f16(10,10))
        
        if s_mw == mw11:
            c1 = choose(w_e,mw11,f16(10,11))      
        
        if s_mw == mw12:
            c1 = choose(w_e,mw12,f16(10,12))
            
        if s_mw == mw13:
            c1 = choose(w_e,mw13,f16(10,13))
        
        if s_mw == mw14:
            c1 = choose(w_e,mw14,f16(10,14))
        
        if s_mw == mw15:
            c1 = choose(w_e,mw15,f16(10,15))      
        
        if s_mw == mw16:
            c1 = choose(w_e,mw16,f16(10,16))
            
        
                 
            
            
    if w_e == w11:
        
        if s_mw == s1:
            c1 = choose(w_e,s1,f16(11,1))
        
        if s_mw == s2:
            c1 = choose(w_e,s2,f16(11,2))
        
        if s_mw == s3:
            c1 = choose(w_e,s3,f16(11,3))      
        
        if s_mw == s4:
            c1 = choose(w_e,s4,f16(11,4))
            
        if s_mw == s5:
            c1 = choose(w_e,s5,f16(11,5))
        
        if s_mw == s6:
            c1 = choose(w_e,s6,f16(11,6))
        
        if s_mw == s7:
            c1 = choose(w_e,s7,f16(11,7))      
        
        if s_mw == s8:
            c1 = choose(w_e,s8,f16(11,8))
            
        if s_mw == s9:
            c1 = choose(w_e,s9,f16(11,9))
        
        if s_mw == s10:
            c1 = choose(w_e,s10,f16(11,10))
        
        if s_mw == s11:
            c1 = choose(w_e,s11,f16(11,11))      
        
        if s_mw == s12:
            c1 = choose(w_e,s12,f16(11,12))
            
        if s_mw == s13:
            c1 = choose(w_e,s13,f16(11,13))
        
        if s_mw == s14:
            c1 = choose(w_e,s14,f16(11,14))
        
        if s_mw == s15:
            c1 = choose(w_e,s15,f16(11,15))      
        
        if s_mw == s16:
            c1 = choose(w_e,s16,f16(11,16))
            
        if s_mw == mw1:
            c1 = choose(w_e,mw1,f16(11,1))
        
        if s_mw == mw2:
            c1 = choose(w_e,mw2,f16(11,2))
        
        if s_mw == mw3:
            c1 = choose(w_e,mw3,f16(11,3))      
        
        if s_mw == mw4:
            c1 = choose(w_e,mw4,f16(11,4))
            
        if s_mw == mw5:
            c1 = choose(w_e,mw5,f16(11,5))
        
        if s_mw == mw6:
            c1 = choose(w_e,mw6,f16(11,6))
        
        if s_mw == mw7:
            c1 = choose(w_e,mw7,f16(11,7))      
        
        if s_mw == mw8:
            c1 = choose(w_e,mw8,f16(11,8))
            
        if s_mw == mw9:
            c1 = choose(w_e,mw9,f16(11,9))
        
        if s_mw == mw10:
            c1 = choose(w_e,mw10,f16(11,10))
        
        if s_mw == mw11:
            c1 = choose(w_e,mw11,f16(11,11))      
        
        if s_mw == mw12:
            c1 = choose(w_e,mw12,f16(11,12))
            
        if s_mw == mw13:
            c1 = choose(w_e,mw13,f16(11,13))
        
        if s_mw == mw14:
            c1 = choose(w_e,mw14,f16(11,14))
        
        if s_mw == mw15:
            c1 = choose(w_e,mw15,f16(11,15))      
        
        if s_mw == mw16:
            c1 = choose(w_e,mw16,f16(11,16))
            
        
                 
            
            
    if w_e == w12:
        
        if s_mw == s1:
            c1 = choose(w_e,s1,f16(12,1))
        
        if s_mw == s2:
            c1 = choose(w_e,s2,f16(12,2))
        
        if s_mw == s3:
            c1 = choose(w_e,s3,f16(12,3))      
        
        if s_mw == s4:
            c1 = choose(w_e,s4,f16(12,4))
            
        if s_mw == s5:
            c1 = choose(w_e,s5,f16(12,5))
        
        if s_mw == s6:
            c1 = choose(w_e,s6,f16(12,6))
        
        if s_mw == s7:
            c1 = choose(w_e,s7,f16(12,7))      
        
        if s_mw == s8:
            c1 = choose(w_e,s8,f16(12,8))
            
        if s_mw == s9:
            c1 = choose(w_e,s9,f16(12,9))
        
        if s_mw == s10:
            c1 = choose(w_e,s10,f16(12,10))
        
        if s_mw == s11:
            c1 = choose(w_e,s11,f16(12,11))      
        
        if s_mw == s12:
            c1 = choose(w_e,s12,f16(12,12))
            
        if s_mw == s13:
            c1 = choose(w_e,s13,f16(12,13))
        
        if s_mw == s14:
            c1 = choose(w_e,s14,f16(12,14))
        
        if s_mw == s15:
            c1 = choose(w_e,s15,f16(12,15))      
        
        if s_mw == s16:
            c1 = choose(w_e,s16,f16(12,16))
            
        if s_mw == mw1:
            c1 = choose(w_e,mw1,f16(12,1))
        
        if s_mw == mw2:
            c1 = choose(w_e,mw2,f16(12,2))
        
        if s_mw == mw3:
            c1 = choose(w_e,mw3,f16(12,3))      
        
        if s_mw == mw4:
            c1 = choose(w_e,mw4,f16(12,4))
            
        if s_mw == mw5:
            c1 = choose(w_e,mw5,f16(12,5))
        
        if s_mw == mw6:
            c1 = choose(w_e,mw6,f16(12,6))
        
        if s_mw == mw7:
            c1 = choose(w_e,mw7,f16(12,7))      
        
        if s_mw == mw8:
            c1 = choose(w_e,mw8,f16(12,8))
            
        if s_mw == mw9:
            c1 = choose(w_e,mw9,f16(12,9))
        
        if s_mw == mw10:
            c1 = choose(w_e,mw10,f16(12,10))
        
        if s_mw == mw11:
            c1 = choose(w_e,mw11,f16(12,11))      
        
        if s_mw == mw12:
            c1 = choose(w_e,mw12,f16(12,12))
            
        if s_mw == mw13:
            c1 = choose(w_e,mw13,f16(12,13))
        
        if s_mw == mw14:
            c1 = choose(w_e,mw14,f16(12,14))
        
        if s_mw == mw15:
            c1 = choose(w_e,mw15,f16(12,15))      
        
        if s_mw == mw16:
            c1 = choose(w_e,mw16,f16(12,16))
            
        
                 
            
            
    if w_e == w13:
        
        if s_mw == s1:
            c1 = choose(w_e,s1,f16(13,1))
        
        if s_mw == s2:
            c1 = choose(w_e,s2,f16(13,2))
        
        if s_mw == s3:
            c1 = choose(w_e,s3,f16(13,3))      
        
        if s_mw == s4:
            c1 = choose(w_e,s4,f16(13,4))
            
        if s_mw == s5:
            c1 = choose(w_e,s5,f16(13,5))
        
        if s_mw == s6:
            c1 = choose(w_e,s6,f16(13,6))
        
        if s_mw == s7:
            c1 = choose(w_e,s7,f16(13,7))      
        
        if s_mw == s8:
            c1 = choose(w_e,s8,f16(13,8))
            
        if s_mw == s9:
            c1 = choose(w_e,s9,f16(13,9))
        
        if s_mw == s10:
            c1 = choose(w_e,s10,f16(13,10))
        
        if s_mw == s11:
            c1 = choose(w_e,s11,f16(13,11))      
        
        if s_mw == s12:
            c1 = choose(w_e,s12,f16(13,12))
            
        if s_mw == s13:
            c1 = choose(w_e,s13,f16(13,13))
        
        if s_mw == s14:
            c1 = choose(w_e,s14,f16(13,14))
        
        if s_mw == s15:
            c1 = choose(w_e,s15,f16(13,15))      
        
        if s_mw == s16:
            c1 = choose(w_e,s16,f16(13,16))
            
        if s_mw == mw1:
            c1 = choose(w_e,mw1,f16(13,1))
        
        if s_mw == mw2:
            c1 = choose(w_e,mw2,f16(13,2))
        
        if s_mw == mw3:
            c1 = choose(w_e,mw3,f16(13,3))      
        
        if s_mw == mw4:
            c1 = choose(w_e,mw4,f16(13,4))
            
        if s_mw == mw5:
            c1 = choose(w_e,mw5,f16(13,5))
        
        if s_mw == mw6:
            c1 = choose(w_e,mw6,f16(13,6))
        
        if s_mw == mw7:
            c1 = choose(w_e,mw7,f16(13,7))      
        
        if s_mw == mw8:
            c1 = choose(w_e,mw8,f16(13,8))
            
        if s_mw == mw9:
            c1 = choose(w_e,mw9,f16(13,9))
        
        if s_mw == mw10:
            c1 = choose(w_e,mw10,f16(13,10))
        
        if s_mw == mw11:
            c1 = choose(w_e,mw11,f16(13,11))      
        
        if s_mw == mw12:
            c1 = choose(w_e,mw12,f16(13,12))
            
        if s_mw == mw13:
            c1 = choose(w_e,mw13,f16(13,13))
        
        if s_mw == mw14:
            c1 = choose(w_e,mw14,f16(13,14))
        
        if s_mw == mw15:
            c1 = choose(w_e,mw15,f16(13,15))      
        
        if s_mw == mw16:
            c1 = choose(w_e,mw16,f16(13,16))
            
        
                 
            
            
    if w_e == w14:
        
        if s_mw == s1:
            c1 = choose(w_e,s1,f16(14,1))
        
        if s_mw == s2:
            c1 = choose(w_e,s2,f16(14,2))
        
        if s_mw == s3:
            c1 = choose(w_e,s3,f16(14,3))      
        
        if s_mw == s4:
            c1 = choose(w_e,s4,f16(14,4))
            
        if s_mw == s5:
            c1 = choose(w_e,s5,f16(14,5))
        
        if s_mw == s6:
            c1 = choose(w_e,s6,f16(14,6))
        
        if s_mw == s7:
            c1 = choose(w_e,s7,f16(14,7))      
        
        if s_mw == s8:
            c1 = choose(w_e,s8,f16(14,8))
            
        if s_mw == s9:
            c1 = choose(w_e,s9,f16(14,9))
        
        if s_mw == s10:
            c1 = choose(w_e,s10,f16(14,10))
        
        if s_mw == s11:
            c1 = choose(w_e,s11,f16(14,11))      
        
        if s_mw == s12:
            c1 = choose(w_e,s12,f16(14,12))
            
        if s_mw == s13:
            c1 = choose(w_e,s13,f16(14,13))
        
        if s_mw == s14:
            c1 = choose(w_e,s14,f16(14,14))
        
        if s_mw == s15:
            c1 = choose(w_e,s15,f16(14,15))      
        
        if s_mw == s16:
            c1 = choose(w_e,s16,f16(14,16))
            
        if s_mw == mw1:
            c1 = choose(w_e,mw1,f16(14,1))
        
        if s_mw == mw2:
            c1 = choose(w_e,mw2,f16(14,2))
        
        if s_mw == mw3:
            c1 = choose(w_e,mw3,f16(14,3))      
        
        if s_mw == mw4:
            c1 = choose(w_e,mw4,f16(14,4))
            
        if s_mw == mw5:
            c1 = choose(w_e,mw5,f16(14,5))
        
        if s_mw == mw6:
            c1 = choose(w_e,mw6,f16(14,6))
        
        if s_mw == mw7:
            c1 = choose(w_e,mw7,f16(14,7))      
        
        if s_mw == mw8:
            c1 = choose(w_e,mw8,f16(14,8))
            
        if s_mw == mw9:
            c1 = choose(w_e,mw9,f16(14,9))
        
        if s_mw == mw10:
            c1 = choose(w_e,mw10,f16(14,10))
        
        if s_mw == mw11:
            c1 = choose(w_e,mw11,f16(14,11))      
        
        if s_mw == mw12:
            c1 = choose(w_e,mw12,f16(14,12))
            
        if s_mw == mw13:
            c1 = choose(w_e,mw13,f16(14,13))
        
        if s_mw == mw14:
            c1 = choose(w_e,mw14,f16(14,14))
        
        if s_mw == mw15:
            c1 = choose(w_e,mw15,f16(14,15))      
        
        if s_mw == mw16:
            c1 = choose(w_e,mw16,f16(14,16))
            
        
                 
            
            
    if w_e == w15:
        
        if s_mw == s1:
            c1 = choose(w_e,s1,f16(15,1))
        
        if s_mw == s2:
            c1 = choose(w_e,s2,f16(15,2))
        
        if s_mw == s3:
            c1 = choose(w_e,s3,f16(15,3))      
        
        if s_mw == s4:
            c1 = choose(w_e,s4,f16(15,4))
            
        if s_mw == s5:
            c1 = choose(w_e,s5,f16(15,5))
        
        if s_mw == s6:
            c1 = choose(w_e,s6,f16(15,6))
        
        if s_mw == s7:
            c1 = choose(w_e,s7,f16(15,7))      
        
        if s_mw == s8:
            c1 = choose(w_e,s8,f16(15,8))
            
        if s_mw == s9:
            c1 = choose(w_e,s9,f16(15,9))
        
        if s_mw == s10:
            c1 = choose(w_e,s10,f16(15,10))
        
        if s_mw == s11:
            c1 = choose(w_e,s11,f16(15,11))      
        
        if s_mw == s12:
            c1 = choose(w_e,s12,f16(15,12))
            
        if s_mw == s13:
            c1 = choose(w_e,s13,f16(15,13))
        
        if s_mw == s14:
            c1 = choose(w_e,s14,f16(15,14))
        
        if s_mw == s15:
            c1 = choose(w_e,s15,f16(15,15))      
        
        if s_mw == s16:
            c1 = choose(w_e,s16,f16(15,16))
            
        if s_mw == mw1:
            c1 = choose(w_e,mw1,f16(15,1))
        
        if s_mw == mw2:
            c1 = choose(w_e,mw2,f16(15,2))
        
        if s_mw == mw3:
            c1 = choose(w_e,mw3,f16(15,3))      
        
        if s_mw == mw4:
            c1 = choose(w_e,mw4,f16(15,4))
            
        if s_mw == mw5:
            c1 = choose(w_e,mw5,f16(15,5))
        
        if s_mw == mw6:
            c1 = choose(w_e,mw6,f16(15,6))
        
        if s_mw == mw7:
            c1 = choose(w_e,mw7,f16(15,7))      
        
        if s_mw == mw8:
            c1 = choose(w_e,mw8,f16(15,8))
            
        if s_mw == mw9:
            c1 = choose(w_e,mw9,f16(15,9))
        
        if s_mw == mw10:
            c1 = choose(w_e,mw10,f16(15,10))
        
        if s_mw == mw11:
            c1 = choose(w_e,mw11,f16(15,11))      
        
        if s_mw == mw12:
            c1 = choose(w_e,mw12,f16(15,12))
            
        if s_mw == mw13:
            c1 = choose(w_e,mw13,f16(15,13))
        
        if s_mw == mw14:
            c1 = choose(w_e,mw14,f16(15,14))
        
        if s_mw == mw15:
            c1 = choose(w_e,mw15,f16(15,15))      
        
        if s_mw == mw16:
            c1 = choose(w_e,mw16,f16(15,16))
            
        
                 
            
            
    if w_e == w16:
        
        if s_mw == s1:
            c1 = choose(w_e,s1,f16(16,1))
        
        if s_mw == s2:
            c1 = choose(w_e,s2,f16(16,2))
        
        if s_mw == s3:
            c1 = choose(w_e,s3,f16(16,3))      
        
        if s_mw == s4:
            c1 = choose(w_e,s4,f16(16,4))
            
        if s_mw == s5:
            c1 = choose(w_e,s5,f16(16,5))
        
        if s_mw == s6:
            c1 = choose(w_e,s6,f16(16,6))
        
        if s_mw == s7:
            c1 = choose(w_e,s7,f16(16,7))      
        
        if s_mw == s8:
            c1 = choose(w_e,s8,f16(16,8))
            
        if s_mw == s9:
            c1 = choose(w_e,s9,f16(16,9))
        
        if s_mw == s10:
            c1 = choose(w_e,s10,f16(16,10))
        
        if s_mw == s11:
            c1 = choose(w_e,s11,f16(16,11))      
        
        if s_mw == s12:
            c1 = choose(w_e,s12,f16(16,12))
            
        if s_mw == s13:
            c1 = choose(w_e,s13,f16(16,13))
        
        if s_mw == s14:
            c1 = choose(w_e,s14,f16(16,14))
        
        if s_mw == s15:
            c1 = choose(w_e,s15,f16(16,15))      
        
        if s_mw == s16:
            c1 = choose(w_e,s16,f16(16,16))
            
        if s_mw == mw1:
            c1 = choose(w_e,mw1,f16(16,1))
        
        if s_mw == mw2:
            c1 = choose(w_e,mw2,f16(16,2))
        
        if s_mw == mw3:
            c1 = choose(w_e,mw3,f16(16,3))      
        
        if s_mw == mw4:
            c1 = choose(w_e,mw4,f16(16,4))
            
        if s_mw == mw5:
            c1 = choose(w_e,mw5,f16(16,5))
        
        if s_mw == mw6:
            c1 = choose(w_e,mw6,f16(16,6))
        
        if s_mw == mw7:
            c1 = choose(w_e,mw7,f16(16,7))      
        
        if s_mw == mw8:
            c1 = choose(w_e,mw8,f16(16,8))
            
        if s_mw == mw9:
            c1 = choose(w_e,mw9,f16(16,9))
        
        if s_mw == mw10:
            c1 = choose(w_e,mw10,f16(16,10))
        
        if s_mw == mw11:
            c1 = choose(w_e,mw11,f16(16,11))      
        
        if s_mw == mw12:
            c1 = choose(w_e,mw12,f16(16,12))
            
        if s_mw == mw13:
            c1 = choose(w_e,mw13,f16(16,13))
        
        if s_mw == mw14:
            c1 = choose(w_e,mw14,f16(16,14))
        
        if s_mw == mw15:
            c1 = choose(w_e,mw15,f16(16,15))      
        
        if s_mw == mw16:
            c1 = choose(w_e,mw16,f16(16,16))
            
        
                 
            
            
    if w_e == e1:
        
        if s_mw == s1:
            c1 = choose(e1,s1,f16(1,1))
        
        if s_mw == s2:
            c1 = choose(e1,s2,f16(1,2))
        
        if s_mw == s3:
            c1 = choose(e1,s3,f16(1,3))      
        
        if s_mw == s4:
            c1 = choose(e1,s4,f16(1,4))
            
        if s_mw == s5:
            c1 = choose(e1,s5,f16(1,5))
        
        if s_mw == s6:
            c1 = choose(e1,s6,f16(1,6))
        
        if s_mw == s7:
            c1 = choose(e1,s7,f16(1,7))      
        
        if s_mw == s8:
            c1 = choose(e1,s8,f16(1,8))
            
        if s_mw == s9:
            c1 = choose(e1,s9,f16(1,9))
        
        if s_mw == s10:
            c1 = choose(e1,s10,f16(1,10))
        
        if s_mw == s11:
            c1 = choose(e1,s11,f16(1,11))      
        
        if s_mw == s12:
            c1 = choose(e1,s12,f16(1,12))
            
        if s_mw == s13:
            c1 = choose(e1,s13,f16(1,13))
        
        if s_mw == s14:
            c1 = choose(e1,s14,f16(1,14))
        
        if s_mw == s15:
            c1 = choose(e1,s15,f16(1,15))      
        
        if s_mw == s16:
            c1 = choose(e1,s16,f16(1,16))
            
        if s_mw == mw1:
            c1 = choose(e1,mw1,f16(1,1))
        
        if s_mw == mw2:
            c1 = choose(e1,mw2,f16(1,2))
        
        if s_mw == mw3:
            c1 = choose(e1,mw3,f16(1,3))      
        
        if s_mw == mw4:
            c1 = choose(e1,mw4,f16(1,4))
            
        if s_mw == mw5:
            c1 = choose(e1,mw5,f16(1,5))
        
        if s_mw == mw6:
            c1 = choose(e1,mw6,f16(1,6))
        
        if s_mw == mw7:
            c1 = choose(e1,mw7,f16(1,7))      
        
        if s_mw == mw8:
            c1 = choose(e1,mw8,f16(1,8))
            
        if s_mw == mw9:
            c1 = choose(e1,mw9,f16(1,9))
        
        if s_mw == mw10:
            c1 = choose(e1,mw10,f16(1,10))
        
        if s_mw == mw11:
            c1 = choose(e1,mw11,f16(1,11))      
        
        if s_mw == mw12:
            c1 = choose(e1,mw12,f16(1,12))
            
        if s_mw == mw13:
            c1 = choose(e1,mw13,f16(1,13))
        
        if s_mw == mw14:
            c1 = choose(e1,mw14,f16(1,14))
        
        if s_mw == mw15:
            c1 = choose(e1,mw15,f16(1,15))      
        
        if s_mw == mw16:
            c1 = choose(e1,mw16,f16(1,16))
            
        
                 
            
            
    if w_e == e2:
        
        if s_mw == s1:
            c1 = choose(e2,s1,f16(2,1))
        
        if s_mw == s2:
            c1 = choose(e2,s2,f16(2,2))
        
        if s_mw == s3:
            c1 = choose(e2,s3,f16(2,3))      
        
        if s_mw == s4:
            c1 = choose(e2,s4,f16(2,4))
            
        if s_mw == s5:
            c1 = choose(e2,s5,f16(2,5))
        
        if s_mw == s6:
            c1 = choose(e2,s6,f16(2,6))
        
        if s_mw == s7:
            c1 = choose(e2,s7,f16(2,7))      
        
        if s_mw == s8:
            c1 = choose(e2,s8,f16(2,8))
            
        if s_mw == s9:
            c1 = choose(e2,s9,f16(2,9))
        
        if s_mw == s10:
            c1 = choose(e2,s10,f16(2,10))
        
        if s_mw == s11:
            c1 = choose(e2,s11,f16(2,11))      
        
        if s_mw == s12:
            c1 = choose(e2,s12,f16(2,12))
            
        if s_mw == s13:
            c1 = choose(e2,s13,f16(2,13))
        
        if s_mw == s14:
            c1 = choose(e2,s14,f16(2,14))
        
        if s_mw == s15:
            c1 = choose(e2,s15,f16(2,15))      
        
        if s_mw == s16:
            c1 = choose(e2,s16,f16(2,16))
            
        if s_mw == mw1:
            c1 = choose(e2,mw1,f16(2,1))
        
        if s_mw == mw2:
            c1 = choose(e2,mw2,f16(2,2))
        
        if s_mw == mw3:
            c1 = choose(e2,mw3,f16(2,3))      
        
        if s_mw == mw4:
            c1 = choose(e2,mw4,f16(2,4))
            
        if s_mw == mw5:
            c1 = choose(e2,mw5,f16(2,5))
        
        if s_mw == mw6:
            c1 = choose(e2,mw6,f16(2,6))
        
        if s_mw == mw7:
            c1 = choose(e2,mw7,f16(2,7))      
        
        if s_mw == mw8:
            c1 = choose(e2,mw8,f16(2,8))
            
        if s_mw == mw9:
            c1 = choose(e2,mw9,f16(2,9))
        
        if s_mw == mw10:
            c1 = choose(e2,mw10,f16(2,10))
        
        if s_mw == mw11:
            c1 = choose(e2,mw11,f16(2,11))      
        
        if s_mw == mw12:
            c1 = choose(e2,mw12,f16(2,12))
            
        if s_mw == mw13:
            c1 = choose(e2,mw13,f16(2,13))
        
        if s_mw == mw14:
            c1 = choose(e2,mw14,f16(2,14))
        
        if s_mw == mw15:
            c1 = choose(e2,mw15,f16(2,15))      
        
        if s_mw == mw16:
            c1 = choose(e2,mw16,f16(2,16))
            
        
                 
            
            
    if w_e == e3:
        
        if s_mw == s1:
            c1 = choose(e3,s1,f16(3,1))
        
        if s_mw == s2:
            c1 = choose(e3,s2,f16(3,2))
        
        if s_mw == s3:
            c1 = choose(e3,s3,f16(3,3))      
        
        if s_mw == s4:
            c1 = choose(e3,s4,f16(3,4))
            
        if s_mw == s5:
            c1 = choose(e3,s5,f16(3,5))
        
        if s_mw == s6:
            c1 = choose(e3,s6,f16(3,6))
        
        if s_mw == s7:
            c1 = choose(e3,s7,f16(3,7))      
        
        if s_mw == s8:
            c1 = choose(e3,s8,f16(3,8))
            
        if s_mw == s9:
            c1 = choose(e3,s9,f16(3,9))
        
        if s_mw == s10:
            c1 = choose(e3,s10,f16(3,10))
        
        if s_mw == s11:
            c1 = choose(e3,s11,f16(3,11))      
        
        if s_mw == s12:
            c1 = choose(e3,s12,f16(3,12))
            
        if s_mw == s13:
            c1 = choose(e3,s13,f16(3,13))
        
        if s_mw == s14:
            c1 = choose(e3,s14,f16(3,14))
        
        if s_mw == s15:
            c1 = choose(e3,s15,f16(3,15))      
        
        if s_mw == s16:
            c1 = choose(e3,s16,f16(3,16))
            
        if s_mw == mw1:
            c1 = choose(e3,mw1,f16(3,1))
        
        if s_mw == mw2:
            c1 = choose(e3,mw2,f16(3,2))
        
        if s_mw == mw3:
            c1 = choose(e3,mw3,f16(3,3))      
        
        if s_mw == mw4:
            c1 = choose(e3,mw4,f16(3,4))
            
        if s_mw == mw5:
            c1 = choose(e3,mw5,f16(3,5))
        
        if s_mw == mw6:
            c1 = choose(e3,mw6,f16(3,6))
        
        if s_mw == mw7:
            c1 = choose(e3,mw7,f16(3,7))      
        
        if s_mw == mw8:
            c1 = choose(e3,mw8,f16(3,8))
            
        if s_mw == mw9:
            c1 = choose(e3,mw9,f16(3,9))
        
        if s_mw == mw10:
            c1 = choose(e3,mw10,f16(3,10))
        
        if s_mw == mw11:
            c1 = choose(e3,mw11,f16(3,11))      
        
        if s_mw == mw12:
            c1 = choose(e3,mw12,f16(3,12))
            
        if s_mw == mw13:
            c1 = choose(e3,mw13,f16(3,13))
        
        if s_mw == mw14:
            c1 = choose(e3,mw14,f16(3,14))
        
        if s_mw == mw15:
            c1 = choose(e3,mw15,f16(3,15))      
        
        if s_mw == mw16:
            c1 = choose(e3,mw16,f16(3,16))
            
        
                 
            
    if w_e == e4:
        
        if s_mw == s1:
            c1 = choose(e4,s1,f16(4,1))
        
        if s_mw == s2:
            c1 = choose(e4,s2,f16(4,2))
        
        if s_mw == s3:
            c1 = choose(e4,s3,f16(4,3))      
        
        if s_mw == s4:
            c1 = choose(e4,s4,f16(4,4))
            
        if s_mw == s5:
            c1 = choose(e4,s5,f16(4,5))
        
        if s_mw == s6:
            c1 = choose(e4,s6,f16(4,6))
        
        if s_mw == s7:
            c1 = choose(e4,s7,f16(4,7))      
        
        if s_mw == s8:
            c1 = choose(e4,s8,f16(4,8))
            
        if s_mw == s9:
            c1 = choose(e4,s9,f16(4,9))
        
        if s_mw == s10:
            c1 = choose(e4,s10,f16(4,10))
        
        if s_mw == s11:
            c1 = choose(e4,s11,f16(4,11))      
        
        if s_mw == s12:
            c1 = choose(e4,s12,f16(4,12))
            
        if s_mw == s13:
            c1 = choose(e4,s13,f16(4,13))
        
        if s_mw == s14:
            c1 = choose(e4,s14,f16(4,14))
        
        if s_mw == s15:
            c1 = choose(e4,s15,f16(4,15))      
        
        if s_mw == s16:
            c1 = choose(e4,s16,f16(4,16))
            
        if s_mw == mw1:
            c1 = choose(e4,mw1,f16(4,1))
        
        if s_mw == mw2:
            c1 = choose(e4,mw2,f16(4,2))
        
        if s_mw == mw3:
            c1 = choose(e4,mw3,f16(4,3))      
        
        if s_mw == mw4:
            c1 = choose(e4,mw4,f16(4,4))
            
        if s_mw == mw5:
            c1 = choose(e4,mw5,f16(4,5))
        
        if s_mw == mw6:
            c1 = choose(e4,mw6,f16(4,6))
        
        if s_mw == mw7:
            c1 = choose(e4,mw7,f16(4,7))      
        
        if s_mw == mw8:
            c1 = choose(e4,mw8,f16(4,8))
            
        if s_mw == mw9:
            c1 = choose(e4,mw9,f16(4,9))
        
        if s_mw == mw10:
            c1 = choose(e4,mw10,f16(4,10))
        
        if s_mw == mw11:
            c1 = choose(e4,mw11,f16(4,11))      
        
        if s_mw == mw12:
            c1 = choose(e4,mw12,f16(4,12))
            
        if s_mw == mw13:
            c1 = choose(e4,mw13,f16(4,13))
        
        if s_mw == mw14:
            c1 = choose(e4,mw14,f16(4,14))
        
        if s_mw == mw15:
            c1 = choose(e4,mw15,f16(4,15))      
        
        if s_mw == mw16:
            c1 = choose(e4,mw16,f16(4,16))
            
        
                 
            
            
    if w_e == e5:
        
        if s_mw == s1:
            c1 = choose(e5,s1,f16(5,1))
        
        if s_mw == s2:
            c1 = choose(e5,s2,f16(5,2))
        
        if s_mw == s3:
            c1 = choose(e5,s3,f16(5,3))      
        
        if s_mw == s4:
            c1 = choose(e5,s4,f16(5,4))
            
        if s_mw == s5:
            c1 = choose(e5,s5,f16(5,5))
        
        if s_mw == s6:
            c1 = choose(e5,s6,f16(5,6))
        
        if s_mw == s7:
            c1 = choose(e5,s7,f16(5,7))      
        
        if s_mw == s8:
            c1 = choose(e5,s8,f16(5,8))
            
        if s_mw == s9:
            c1 = choose(e5,s9,f16(5,9))
        
        if s_mw == s10:
            c1 = choose(e5,s10,f16(5,10))
        
        if s_mw == s11:
            c1 = choose(e5,s11,f16(5,11))      
        
        if s_mw == s12:
            c1 = choose(e5,s12,f16(5,12))
            
        if s_mw == s13:
            c1 = choose(e5,s13,f16(5,13))
        
        if s_mw == s14:
            c1 = choose(e5,s14,f16(5,14))
        
        if s_mw == s15:
            c1 = choose(e5,s15,f16(5,15))      
        
        if s_mw == s16:
            c1 = choose(e5,s16,f16(5,16))
            
        if s_mw == mw1:
            c1 = choose(e5,mw1,f16(5,1))
        
        if s_mw == mw2:
            c1 = choose(e5,mw2,f16(5,2))
        
        if s_mw == mw3:
            c1 = choose(e5,mw3,f16(5,3))      
        
        if s_mw == mw4:
            c1 = choose(e5,mw4,f16(5,4))
            
        if s_mw == mw5:
            c1 = choose(e5,mw5,f16(5,5))
        
        if s_mw == mw6:
            c1 = choose(e5,mw6,f16(5,6))
        
        if s_mw == mw7:
            c1 = choose(e5,mw7,f16(5,7))      
        
        if s_mw == mw8:
            c1 = choose(e5,mw8,f16(5,8))
            
        if s_mw == mw9:
            c1 = choose(e5,mw9,f16(5,9))
        
        if s_mw == mw10:
            c1 = choose(e5,mw10,f16(5,10))
        
        if s_mw == mw11:
            c1 = choose(e5,mw11,f16(5,11))      
        
        if s_mw == mw12:
            c1 = choose(e5,mw12,f16(5,12))
            
        if s_mw == mw13:
            c1 = choose(e5,mw13,f16(5,13))
        
        if s_mw == mw14:
            c1 = choose(e5,mw14,f16(5,14))
        
        if s_mw == mw15:
            c1 = choose(e5,mw15,f16(5,15))      
        
        if s_mw == mw16:
            c1 = choose(e5,mw16,f16(5,16))
            
        
                 
            
            
    if w_e == e6:
        
        if s_mw == s1:
            c1 = choose(e6,s1,f16(6,1))
        
        if s_mw == s2:
            c1 = choose(e6,s2,f16(6,2))
        
        if s_mw == s3:
            c1 = choose(e6,s3,f16(6,3))      
        
        if s_mw == s4:
            c1 = choose(e6,s4,f16(6,4))
            
        if s_mw == s5:
            c1 = choose(e6,s5,f16(6,5))
        
        if s_mw == s6:
            c1 = choose(e6,s6,f16(6,6))
        
        if s_mw == s7:
            c1 = choose(e6,s7,f16(6,7))      
        
        if s_mw == s8:
            c1 = choose(e6,s8,f16(6,8))
            
        if s_mw == s9:
            c1 = choose(e6,s9,f16(6,9))
        
        if s_mw == s10:
            c1 = choose(e6,s10,f16(6,10))
        
        if s_mw == s11:
            c1 = choose(e6,s11,f16(6,11))      
        
        if s_mw == s12:
            c1 = choose(e6,s12,f16(6,12))
            
        if s_mw == s13:
            c1 = choose(e6,s13,f16(6,13))
        
        if s_mw == s14:
            c1 = choose(e6,s14,f16(6,14))
        
        if s_mw == s15:
            c1 = choose(e6,s15,f16(6,15))      
        
        if s_mw == s16:
            c1 = choose(e6,s16,f16(6,16))
            
        if s_mw == mw1:
            c1 = choose(e6,mw1,f16(6,1))
        
        if s_mw == mw2:
            c1 = choose(e6,mw2,f16(6,2))
        
        if s_mw == mw3:
            c1 = choose(e6,mw3,f16(6,3))      
        
        if s_mw == mw4:
            c1 = choose(e6,mw4,f16(6,4))
            
        if s_mw == mw5:
            c1 = choose(e6,mw5,f16(6,5))
        
        if s_mw == mw6:
            c1 = choose(e6,mw6,f16(6,6))
        
        if s_mw == mw7:
            c1 = choose(e6,mw7,f16(6,7))      
        
        if s_mw == mw8:
            c1 = choose(e6,mw8,f16(6,8))
            
        if s_mw == mw9:
            c1 = choose(e6,mw9,f16(6,9))
        
        if s_mw == mw10:
            c1 = choose(e6,mw10,f16(6,10))
        
        if s_mw == mw11:
            c1 = choose(e6,mw11,f16(6,11))      
        
        if s_mw == mw12:
            c1 = choose(e6,mw12,f16(6,12))
            
        if s_mw == mw13:
            c1 = choose(e6,mw13,f16(6,13))
        
        if s_mw == mw14:
            c1 = choose(e6,mw14,f16(6,14))
        
        if s_mw == mw15:
            c1 = choose(e6,mw15,f16(6,15))      
        
        if s_mw == mw16:
            c1 = choose(e6,mw16,f16(6,16))
            
        
                 
            
            
    if w_e == e7:
        
        if s_mw == s1:
            c1 = choose(e7,s1,f16(7,1))
        
        if s_mw == s2:
            c1 = choose(e7,s2,f16(7,2))
        
        if s_mw == s3:
            c1 = choose(e7,s3,f16(7,3))      
        
        if s_mw == s4:
            c1 = choose(e7,s4,f16(7,4))
            
        if s_mw == s5:
            c1 = choose(e7,s5,f16(7,5))
        
        if s_mw == s6:
            c1 = choose(e7,s6,f16(7,6))
        
        if s_mw == s7:
            c1 = choose(e7,s7,f16(7,7))      
        
        if s_mw == s8:
            c1 = choose(e7,s8,f16(7,8))
            
        if s_mw == s9:
            c1 = choose(e7,s9,f16(7,9))
        
        if s_mw == s10:
            c1 = choose(e7,s10,f16(7,10))
        
        if s_mw == s11:
            c1 = choose(e7,s11,f16(7,11))      
        
        if s_mw == s12:
            c1 = choose(e7,s12,f16(7,12))
            
        if s_mw == s13:
            c1 = choose(e7,s13,f16(7,13))
        
        if s_mw == s14:
            c1 = choose(e7,s14,f16(7,14))
        
        if s_mw == s15:
            c1 = choose(e7,s15,f16(7,15))      
        
        if s_mw == s16:
            c1 = choose(e7,s16,f16(7,16))
            
        if s_mw == mw1:
            c1 = choose(e7,mw1,f16(7,1))
        
        if s_mw == mw2:
            c1 = choose(e7,mw2,f16(7,2))
        
        if s_mw == mw3:
            c1 = choose(e7,mw3,f16(7,3))      
        
        if s_mw == mw4:
            c1 = choose(e7,mw4,f16(7,4))
            
        if s_mw == mw5:
            c1 = choose(e7,mw5,f16(7,5))
        
        if s_mw == mw6:
            c1 = choose(e7,mw6,f16(7,6))
        
        if s_mw == mw7:
            c1 = choose(e7,mw7,f16(7,7))      
        
        if s_mw == mw8:
            c1 = choose(e7,mw8,f16(7,8))
            
        if s_mw == mw9:
            c1 = choose(e7,mw9,f16(7,9))
        
        if s_mw == mw10:
            c1 = choose(e7,mw10,f16(7,10))
        
        if s_mw == mw11:
            c1 = choose(e7,mw11,f16(7,11))      
        
        if s_mw == mw12:
            c1 = choose(e7,mw12,f16(7,12))
            
        if s_mw == mw13:
            c1 = choose(e7,mw13,f16(7,13))
        
        if s_mw == mw14:
            c1 = choose(e7,mw14,f16(7,14))
        
        if s_mw == mw15:
            c1 = choose(e7,mw15,f16(7,15))      
        
        if s_mw == mw16:
            c1 = choose(e7,mw16,f16(7,16))
            
        
                 
            
            
    if w_e == e8:
        
        if s_mw == s1:
            c1 = choose(w_e,s1,f16(8,1))
        
        if s_mw == s2:
            c1 = choose(w_e,s2,f16(8,2))
        
        if s_mw == s3:
            c1 = choose(w_e,s3,f16(8,3))      
        
        if s_mw == s4:
            c1 = choose(w_e,s4,f16(8,4))
            
        if s_mw == s5:
            c1 = choose(w_e,s5,f16(8,5))
        
        if s_mw == s6:
            c1 = choose(w_e,s6,f16(8,6))
        
        if s_mw == s7:
            c1 = choose(w_e,s7,f16(8,7))      
        
        if s_mw == s8:
            c1 = choose(w_e,s8,f16(8,8))
            
        if s_mw == s9:
            c1 = choose(w_e,s9,f16(8,9))
        
        if s_mw == s10:
            c1 = choose(w_e,s10,f16(8,10))
        
        if s_mw == s11:
            c1 = choose(w_e,s11,f16(8,11))      
        
        if s_mw == s12:
            c1 = choose(w_e,s12,f16(8,12))
            
        if s_mw == s13:
            c1 = choose(w_e,s13,f16(8,13))
        
        if s_mw == s14:
            c1 = choose(w_e,s14,f16(8,14))
        
        if s_mw == s15:
            c1 = choose(w_e,s15,f16(8,15))      
        
        if s_mw == s16:
            c1 = choose(w_e,s16,f16(8,16))
            
        if s_mw == mw1:
            c1 = choose(w_e,mw1,f16(8,1))
        
        if s_mw == mw2:
            c1 = choose(w_e,mw2,f16(8,2))
        
        if s_mw == mw3:
            c1 = choose(w_e,mw3,f16(8,3))      
        
        if s_mw == mw4:
            c1 = choose(w_e,mw4,f16(8,4))
            
        if s_mw == mw5:
            c1 = choose(w_e,mw5,f16(8,5))
        
        if s_mw == mw6:
            c1 = choose(w_e,mw6,f16(8,6))
        
        if s_mw == mw7:
            c1 = choose(w_e,mw7,f16(8,7))      
        
        if s_mw == mw8:
            c1 = choose(w_e,mw8,f16(8,8))
            
        if s_mw == mw9:
            c1 = choose(w_e,mw9,f16(8,9))
        
        if s_mw == mw10:
            c1 = choose(w_e,mw10,f16(8,10))
        
        if s_mw == mw11:
            c1 = choose(w_e,mw11,f16(8,11))      
        
        if s_mw == mw12:
            c1 = choose(w_e,mw12,f16(8,12))
            
        if s_mw == mw13:
            c1 = choose(w_e,mw13,f16(8,13))
        
        if s_mw == mw14:
            c1 = choose(w_e,mw14,f16(8,14))
        
        if s_mw == mw15:
            c1 = choose(w_e,mw15,f16(8,15))      
        
        if s_mw == mw16:
            c1 = choose(w_e,mw16,f16(8,16))
            
        
                 
            
            
    if w_e == e9:
        
        if s_mw == s1:
            c1 = choose(w_e,s1,f16(9,1))
        
        if s_mw == s2:
            c1 = choose(w_e,s2,f16(9,2))
        
        if s_mw == s3:
            c1 = choose(w_e,s3,f16(9,3))      
        
        if s_mw == s4:
            c1 = choose(w_e,s4,f16(9,4))
            
        if s_mw == s5:
            c1 = choose(w_e,s5,f16(9,5))
        
        if s_mw == s6:
            c1 = choose(w_e,s6,f16(9,6))
        
        if s_mw == s7:
            c1 = choose(w_e,s7,f16(9,7))      
        
        if s_mw == s8:
            c1 = choose(w_e,s8,f16(9,8))
            
        if s_mw == s9:
            c1 = choose(w_e,s9,f16(9,9))
        
        if s_mw == s10:
            c1 = choose(w_e,s10,f16(9,10))
        
        if s_mw == s11:
            c1 = choose(w_e,s11,f16(9,11))      
        
        if s_mw == s12:
            c1 = choose(w_e,s12,f16(9,12))
            
        if s_mw == s13:
            c1 = choose(w_e,s13,f16(9,13))
        
        if s_mw == s14:
            c1 = choose(w_e,s14,f16(9,14))
        
        if s_mw == s15:
            c1 = choose(w_e,s15,f16(9,15))      
        
        if s_mw == s16:
            c1 = choose(w_e,s16,f16(9,16))
            
        if s_mw == mw1:
            c1 = choose(w_e,mw1,f16(9,1))
        
        if s_mw == mw2:
            c1 = choose(w_e,mw2,f16(9,2))
        
        if s_mw == mw3:
            c1 = choose(w_e,mw3,f16(9,3))      
        
        if s_mw == mw4:
            c1 = choose(w_e,mw4,f16(9,4))
            
        if s_mw == mw5:
            c1 = choose(w_e,mw5,f16(9,5))
        
        if s_mw == mw6:
            c1 = choose(w_e,mw6,f16(9,6))
        
        if s_mw == mw7:
            c1 = choose(w_e,mw7,f16(9,7))      
        
        if s_mw == mw8:
            c1 = choose(w_e,mw8,f16(9,8))
            
        if s_mw == mw9:
            c1 = choose(w_e,mw9,f16(9,9))
        
        if s_mw == mw10:
            c1 = choose(w_e,mw10,f16(9,10))
        
        if s_mw == mw11:
            c1 = choose(w_e,mw11,f16(9,11))      
        
        if s_mw == mw12:
            c1 = choose(w_e,mw12,f16(9,12))
            
        if s_mw == mw13:
            c1 = choose(w_e,mw13,f16(9,13))
        
        if s_mw == mw14:
            c1 = choose(w_e,mw14,f16(9,14))
        
        if s_mw == mw15:
            c1 = choose(w_e,mw15,f16(9,15))      
        
        if s_mw == mw16:
            c1 = choose(w_e,mw16,f16(9,16))
            
        
                 
            
            
    if w_e == e10:
        
        if s_mw == s1:
            c1 = choose(w_e,s1,f16(10,1))
        
        if s_mw == s2:
            c1 = choose(w_e,s2,f16(10,2))
        
        if s_mw == s3:
            c1 = choose(w_e,s3,f16(10,3))      
        
        if s_mw == s4:
            c1 = choose(w_e,s4,f16(10,4))
            
        if s_mw == s5:
            c1 = choose(w_e,s5,f16(10,5))
        
        if s_mw == s6:
            c1 = choose(w_e,s6,f16(10,6))
        
        if s_mw == s7:
            c1 = choose(w_e,s7,f16(10,7))      
        
        if s_mw == s8:
            c1 = choose(w_e,s8,f16(10,8))
            
        if s_mw == s9:
            c1 = choose(w_e,s9,f16(10,9))
        
        if s_mw == s10:
            c1 = choose(w_e,s10,f16(10,10))
        
        if s_mw == s11:
            c1 = choose(w_e,s11,f16(10,11))      
        
        if s_mw == s12:
            c1 = choose(w_e,s12,f16(10,12))
            
        if s_mw == s13:
            c1 = choose(w_e,s13,f16(10,13))
        
        if s_mw == s14:
            c1 = choose(w_e,s14,f16(10,14))
        
        if s_mw == s15:
            c1 = choose(w_e,s15,f16(10,15))      
        
        if s_mw == s16:
            c1 = choose(w_e,s16,f16(10,16))
            
        if s_mw == mw1:
            c1 = choose(w_e,mw1,f16(10,1))
        
        if s_mw == mw2:
            c1 = choose(w_e,mw2,f16(10,2))
        
        if s_mw == mw3:
            c1 = choose(w_e,mw3,f16(10,3))      
        
        if s_mw == mw4:
            c1 = choose(w_e,mw4,f16(10,4))
            
        if s_mw == mw5:
            c1 = choose(w_e,mw5,f16(10,5))
        
        if s_mw == mw6:
            c1 = choose(w_e,mw6,f16(10,6))
        
        if s_mw == mw7:
            c1 = choose(w_e,mw7,f16(10,7))      
        
        if s_mw == mw8:
            c1 = choose(w_e,mw8,f16(10,8))
            
        if s_mw == mw9:
            c1 = choose(w_e,mw9,f16(10,9))
        
        if s_mw == mw10:
            c1 = choose(w_e,mw10,f16(10,10))
        
        if s_mw == mw11:
            c1 = choose(w_e,mw11,f16(10,11))      
        
        if s_mw == mw12:
            c1 = choose(w_e,mw12,f16(10,12))
            
        if s_mw == mw13:
            c1 = choose(w_e,mw13,f16(10,13))
        
        if s_mw == mw14:
            c1 = choose(w_e,mw14,f16(10,14))
        
        if s_mw == mw15:
            c1 = choose(w_e,mw15,f16(10,15))      
        
        if s_mw == mw16:
            c1 = choose(w_e,mw16,f16(10,16))
            
        
                 
            
            
    if w_e == e11:
        
        if s_mw == s1:
            c1 = choose(w_e,s1,f16(11,1))
        
        if s_mw == s2:
            c1 = choose(w_e,s2,f16(11,2))
        
        if s_mw == s3:
            c1 = choose(w_e,s3,f16(11,3))      
        
        if s_mw == s4:
            c1 = choose(w_e,s4,f16(11,4))
            
        if s_mw == s5:
            c1 = choose(w_e,s5,f16(11,5))
        
        if s_mw == s6:
            c1 = choose(w_e,s6,f16(11,6))
        
        if s_mw == s7:
            c1 = choose(w_e,s7,f16(11,7))      
        
        if s_mw == s8:
            c1 = choose(w_e,s8,f16(11,8))
            
        if s_mw == s9:
            c1 = choose(w_e,s9,f16(11,9))
        
        if s_mw == s10:
            c1 = choose(w_e,s10,f16(11,10))
        
        if s_mw == s11:
            c1 = choose(w_e,s11,f16(11,11))      
        
        if s_mw == s12:
            c1 = choose(w_e,s12,f16(11,12))
            
        if s_mw == s13:
            c1 = choose(w_e,s13,f16(11,13))
        
        if s_mw == s14:
            c1 = choose(w_e,s14,f16(11,14))
        
        if s_mw == s15:
            c1 = choose(w_e,s15,f16(11,15))      
        
        if s_mw == s16:
            c1 = choose(w_e,s16,f16(11,16))
            
        if s_mw == mw1:
            c1 = choose(w_e,mw1,f16(11,1))
        
        if s_mw == mw2:
            c1 = choose(w_e,mw2,f16(11,2))
        
        if s_mw == mw3:
            c1 = choose(w_e,mw3,f16(11,3))      
        
        if s_mw == mw4:
            c1 = choose(w_e,mw4,f16(11,4))
            
        if s_mw == mw5:
            c1 = choose(w_e,mw5,f16(11,5))
        
        if s_mw == mw6:
            c1 = choose(w_e,mw6,f16(11,6))
        
        if s_mw == mw7:
            c1 = choose(w_e,mw7,f16(11,7))      
        
        if s_mw == mw8:
            c1 = choose(w_e,mw8,f16(11,8))
            
        if s_mw == mw9:
            c1 = choose(w_e,mw9,f16(11,9))
        
        if s_mw == mw10:
            c1 = choose(w_e,mw10,f16(11,10))
        
        if s_mw == mw11:
            c1 = choose(w_e,mw11,f16(11,11))      
        
        if s_mw == mw12:
            c1 = choose(w_e,mw12,f16(11,12))
            
        if s_mw == mw13:
            c1 = choose(w_e,mw13,f16(11,13))
        
        if s_mw == mw14:
            c1 = choose(w_e,mw14,f16(11,14))
        
        if s_mw == mw15:
            c1 = choose(w_e,mw15,f16(11,15))      
        
        if s_mw == mw16:
            c1 = choose(w_e,mw16,f16(11,16))
            
        
                 
            
            
    if w_e == e12:
        
        if s_mw == s1:
            c1 = choose(w_e,s1,f16(12,1))
        
        if s_mw == s2:
            c1 = choose(w_e,s2,f16(12,2))
        
        if s_mw == s3:
            c1 = choose(w_e,s3,f16(12,3))      
        
        if s_mw == s4:
            c1 = choose(w_e,s4,f16(12,4))
            
        if s_mw == s5:
            c1 = choose(w_e,s5,f16(12,5))
        
        if s_mw == s6:
            c1 = choose(w_e,s6,f16(12,6))
        
        if s_mw == s7:
            c1 = choose(w_e,s7,f16(12,7))      
        
        if s_mw == s8:
            c1 = choose(w_e,s8,f16(12,8))
            
        if s_mw == s9:
            c1 = choose(w_e,s9,f16(12,9))
        
        if s_mw == s10:
            c1 = choose(w_e,s10,f16(12,10))
        
        if s_mw == s11:
            c1 = choose(w_e,s11,f16(12,11))      
        
        if s_mw == s12:
            c1 = choose(w_e,s12,f16(12,12))
            
        if s_mw == s13:
            c1 = choose(w_e,s13,f16(12,13))
        
        if s_mw == s14:
            c1 = choose(w_e,s14,f16(12,14))
        
        if s_mw == s15:
            c1 = choose(w_e,s15,f16(12,15))      
        
        if s_mw == s16:
            c1 = choose(w_e,s16,f16(12,16))
            
        if s_mw == mw1:
            c1 = choose(w_e,mw1,f16(12,1))
        
        if s_mw == mw2:
            c1 = choose(w_e,mw2,f16(12,2))
        
        if s_mw == mw3:
            c1 = choose(w_e,mw3,f16(12,3))      
        
        if s_mw == mw4:
            c1 = choose(w_e,mw4,f16(12,4))
            
        if s_mw == mw5:
            c1 = choose(w_e,mw5,f16(12,5))
        
        if s_mw == mw6:
            c1 = choose(w_e,mw6,f16(12,6))
        
        if s_mw == mw7:
            c1 = choose(w_e,mw7,f16(12,7))      
        
        if s_mw == mw8:
            c1 = choose(w_e,mw8,f16(12,8))
            
        if s_mw == mw9:
            c1 = choose(w_e,mw9,f16(12,9))
        
        if s_mw == mw10:
            c1 = choose(w_e,mw10,f16(12,10))
        
        if s_mw == mw11:
            c1 = choose(w_e,mw11,f16(12,11))      
        
        if s_mw == mw12:
            c1 = choose(w_e,mw12,f16(12,12))
            
        if s_mw == mw13:
            c1 = choose(w_e,mw13,f16(12,13))
        
        if s_mw == mw14:
            c1 = choose(w_e,mw14,f16(12,14))
        
        if s_mw == mw15:
            c1 = choose(w_e,mw15,f16(12,15))      
        
        if s_mw == mw16:
            c1 = choose(w_e,mw16,f16(12,16))
            
        
                 
            
            
    if w_e == e13:
        
        if s_mw == s1:
            c1 = choose(w_e,s1,f16(13,1))
        
        if s_mw == s2:
            c1 = choose(w_e,s2,f16(13,2))
        
        if s_mw == s3:
            c1 = choose(w_e,s3,f16(13,3))      
        
        if s_mw == s4:
            c1 = choose(w_e,s4,f16(13,4))
            
        if s_mw == s5:
            c1 = choose(w_e,s5,f16(13,5))
        
        if s_mw == s6:
            c1 = choose(w_e,s6,f16(13,6))
        
        if s_mw == s7:
            c1 = choose(w_e,s7,f16(13,7))      
        
        if s_mw == s8:
            c1 = choose(w_e,s8,f16(13,8))
            
        if s_mw == s9:
            c1 = choose(w_e,s9,f16(13,9))
        
        if s_mw == s10:
            c1 = choose(w_e,s10,f16(13,10))
        
        if s_mw == s11:
            c1 = choose(w_e,s11,f16(13,11))      
        
        if s_mw == s12:
            c1 = choose(w_e,s12,f16(13,12))
            
        if s_mw == s13:
            c1 = choose(w_e,s13,f16(13,13))
        
        if s_mw == s14:
            c1 = choose(w_e,s14,f16(13,14))
        
        if s_mw == s15:
            c1 = choose(w_e,s15,f16(13,15))      
        
        if s_mw == s16:
            c1 = choose(w_e,s16,f16(13,16))
            
        if s_mw == mw1:
            c1 = choose(w_e,mw1,f16(13,1))
        
        if s_mw == mw2:
            c1 = choose(w_e,mw2,f16(13,2))
        
        if s_mw == mw3:
            c1 = choose(w_e,mw3,f16(13,3))      
        
        if s_mw == mw4:
            c1 = choose(w_e,mw4,f16(13,4))
            
        if s_mw == mw5:
            c1 = choose(w_e,mw5,f16(13,5))
        
        if s_mw == mw6:
            c1 = choose(w_e,mw6,f16(13,6))
        
        if s_mw == mw7:
            c1 = choose(w_e,mw7,f16(13,7))      
        
        if s_mw == mw8:
            c1 = choose(w_e,mw8,f16(13,8))
            
        if s_mw == mw9:
            c1 = choose(w_e,mw9,f16(13,9))
        
        if s_mw == mw10:
            c1 = choose(w_e,mw10,f16(13,10))
        
        if s_mw == mw11:
            c1 = choose(w_e,mw11,f16(13,11))      
        
        if s_mw == mw12:
            c1 = choose(w_e,mw12,f16(13,12))
            
        if s_mw == mw13:
            c1 = choose(w_e,mw13,f16(13,13))
        
        if s_mw == mw14:
            c1 = choose(w_e,mw14,f16(13,14))
        
        if s_mw == mw15:
            c1 = choose(w_e,mw15,f16(13,15))      
        
        if s_mw == mw16:
            c1 = choose(w_e,mw16,f16(13,16))
            
        
                 
            
            
    if w_e == e14:
        
        if s_mw == s1:
            c1 = choose(w_e,s1,f16(14,1))
        
        if s_mw == s2:
            c1 = choose(w_e,s2,f16(14,2))
        
        if s_mw == s3:
            c1 = choose(w_e,s3,f16(14,3))      
        
        if s_mw == s4:
            c1 = choose(w_e,s4,f16(14,4))
            
        if s_mw == s5:
            c1 = choose(w_e,s5,f16(14,5))
        
        if s_mw == s6:
            c1 = choose(w_e,s6,f16(14,6))
        
        if s_mw == s7:
            c1 = choose(w_e,s7,f16(14,7))      
        
        if s_mw == s8:
            c1 = choose(w_e,s8,f16(14,8))
            
        if s_mw == s9:
            c1 = choose(w_e,s9,f16(14,9))
        
        if s_mw == s10:
            c1 = choose(w_e,s10,f16(14,10))
        
        if s_mw == s11:
            c1 = choose(w_e,s11,f16(14,11))      
        
        if s_mw == s12:
            c1 = choose(w_e,s12,f16(14,12))
            
        if s_mw == s13:
            c1 = choose(w_e,s13,f16(14,13))
        
        if s_mw == s14:
            c1 = choose(w_e,s14,f16(14,14))
        
        if s_mw == s15:
            c1 = choose(w_e,s15,f16(14,15))      
        
        if s_mw == s16:
            c1 = choose(w_e,s16,f16(14,16))
            
        if s_mw == mw1:
            c1 = choose(w_e,mw1,f16(14,1))
        
        if s_mw == mw2:
            c1 = choose(w_e,mw2,f16(14,2))
        
        if s_mw == mw3:
            c1 = choose(w_e,mw3,f16(14,3))      
        
        if s_mw == mw4:
            c1 = choose(w_e,mw4,f16(14,4))
            
        if s_mw == mw5:
            c1 = choose(w_e,mw5,f16(14,5))
        
        if s_mw == mw6:
            c1 = choose(w_e,mw6,f16(14,6))
        
        if s_mw == mw7:
            c1 = choose(w_e,mw7,f16(14,7))      
        
        if s_mw == mw8:
            c1 = choose(w_e,mw8,f16(14,8))
            
        if s_mw == mw9:
            c1 = choose(w_e,mw9,f16(14,9))
        
        if s_mw == mw10:
            c1 = choose(w_e,mw10,f16(14,10))
        
        if s_mw == mw11:
            c1 = choose(w_e,mw11,f16(14,11))      
        
        if s_mw == mw12:
            c1 = choose(w_e,mw12,f16(14,12))
            
        if s_mw == mw13:
            c1 = choose(w_e,mw13,f16(14,13))
        
        if s_mw == mw14:
            c1 = choose(w_e,mw14,f16(14,14))
        
        if s_mw == mw15:
            c1 = choose(w_e,mw15,f16(14,15))      
        
        if s_mw == mw16:
            c1 = choose(w_e,mw16,f16(14,16))
            
        
                 
            
            
    if w_e == e15:
        
        if s_mw == s1:
            c1 = choose(w_e,s1,f16(15,1))
        
        if s_mw == s2:
            c1 = choose(w_e,s2,f16(15,2))
        
        if s_mw == s3:
            c1 = choose(w_e,s3,f16(15,3))      
        
        if s_mw == s4:
            c1 = choose(w_e,s4,f16(15,4))
            
        if s_mw == s5:
            c1 = choose(w_e,s5,f16(15,5))
        
        if s_mw == s6:
            c1 = choose(w_e,s6,f16(15,6))
        
        if s_mw == s7:
            c1 = choose(w_e,s7,f16(15,7))      
        
        if s_mw == s8:
            c1 = choose(w_e,s8,f16(15,8))
            
        if s_mw == s9:
            c1 = choose(w_e,s9,f16(15,9))
        
        if s_mw == s10:
            c1 = choose(w_e,s10,f16(15,10))
        
        if s_mw == s11:
            c1 = choose(w_e,s11,f16(15,11))      
        
        if s_mw == s12:
            c1 = choose(w_e,s12,f16(15,12))
            
        if s_mw == s13:
            c1 = choose(w_e,s13,f16(15,13))
        
        if s_mw == s14:
            c1 = choose(w_e,s14,f16(15,14))
        
        if s_mw == s15:
            c1 = choose(w_e,s15,f16(15,15))      
        
        if s_mw == s16:
            c1 = choose(w_e,s16,f16(15,16))
            
        if s_mw == mw1:
            c1 = choose(w_e,mw1,f16(15,1))
        
        if s_mw == mw2:
            c1 = choose(w_e,mw2,f16(15,2))
        
        if s_mw == mw3:
            c1 = choose(w_e,mw3,f16(15,3))      
        
        if s_mw == mw4:
            c1 = choose(w_e,mw4,f16(15,4))
            
        if s_mw == mw5:
            c1 = choose(w_e,mw5,f16(15,5))
        
        if s_mw == mw6:
            c1 = choose(w_e,mw6,f16(15,6))
        
        if s_mw == mw7:
            c1 = choose(w_e,mw7,f16(15,7))      
        
        if s_mw == mw8:
            c1 = choose(w_e,mw8,f16(15,8))
            
        if s_mw == mw9:
            c1 = choose(w_e,mw9,f16(15,9))
        
        if s_mw == mw10:
            c1 = choose(w_e,mw10,f16(15,10))
        
        if s_mw == mw11:
            c1 = choose(w_e,mw11,f16(15,11))      
        
        if s_mw == mw12:
            c1 = choose(w_e,mw12,f16(15,12))
            
        if s_mw == mw13:
            c1 = choose(w_e,mw13,f16(15,13))
        
        if s_mw == mw14:
            c1 = choose(w_e,mw14,f16(15,14))
        
        if s_mw == mw15:
            c1 = choose(w_e,mw15,f16(15,15))      
        
        if s_mw == mw16:
            c1 = choose(w_e,mw16,f16(15,16))
            
        
                 
            
            
    if w_e == e16:
        
        if s_mw == s1:
            c1 = choose(w_e,s1,f16(16,1))
        
        if s_mw == s2:
            c1 = choose(w_e,s2,f16(16,2))
        
        if s_mw == s3:
            c1 = choose(w_e,s3,f16(16,3))      
        
        if s_mw == s4:
            c1 = choose(w_e,s4,f16(16,4))
            
        if s_mw == s5:
            c1 = choose(w_e,s5,f16(16,5))
        
        if s_mw == s6:
            c1 = choose(w_e,s6,f16(16,6))
        
        if s_mw == s7:
            c1 = choose(w_e,s7,f16(16,7))      
        
        if s_mw == s8:
            c1 = choose(w_e,s8,f16(16,8))
            
        if s_mw == s9:
            c1 = choose(w_e,s9,f16(16,9))
        
        if s_mw == s10:
            c1 = choose(w_e,s10,f16(16,10))
        
        if s_mw == s11:
            c1 = choose(w_e,s11,f16(16,11))      
        
        if s_mw == s12:
            c1 = choose(w_e,s12,f16(16,12))
            
        if s_mw == s13:
            c1 = choose(w_e,s13,f16(16,13))
        
        if s_mw == s14:
            c1 = choose(w_e,s14,f16(16,14))
        
        if s_mw == s15:
            c1 = choose(w_e,s15,f16(16,15))      
        
        if s_mw == s16:
            c1 = choose(w_e,s16,f16(16,16))
            
        if s_mw == mw1:
            c1 = choose(w_e,mw1,f16(16,1))
        
        if s_mw == mw2:
            c1 = choose(w_e,mw2,f16(16,2))
        
        if s_mw == mw3:
            c1 = choose(w_e,mw3,f16(16,3))      
        
        if s_mw == mw4:
            c1 = choose(w_e,mw4,f16(16,4))
            
        if s_mw == mw5:
            c1 = choose(w_e,mw5,f16(16,5))
        
        if s_mw == mw6:
            c1 = choose(w_e,mw6,f16(16,6))
        
        if s_mw == mw7:
            c1 = choose(w_e,mw7,f16(16,7))      
        
        if s_mw == mw8:
            c1 = choose(w_e,mw8,f16(16,8))
            
        if s_mw == mw9:
            c1 = choose(w_e,mw9,f16(16,9))
        
        if s_mw == mw10:
            c1 = choose(w_e,mw10,f16(16,10))
        
        if s_mw == mw11:
            c1 = choose(w_e,mw11,f16(16,11))      
        
        if s_mw == mw12:
            c1 = choose(w_e,mw12,f16(16,12))
            
        if s_mw == mw13:
            c1 = choose(w_e,mw13,f16(16,13))
        
        if s_mw == mw14:
            c1 = choose(w_e,mw14,f16(16,14))
        
        if s_mw == mw15:
            c1 = choose(w_e,mw15,f16(16,15))      
        
        if s_mw == mw16:
            c1 = choose(w_e,mw16,f16(16,16))
            
        
                 
    print('Your national champion...')        
    print(c1)
    print('...')



    return c1



# champ = createBracket()

# while champ != 'San Diego St.':
    
#       champ = createBracket()


#-------------------------------#


# b = np.arange(0,1000)
# SDSU = 0

# for i in b:
    
#     champ = createBracket()
    
#     if champ == 'San Diego St.':
    
#         SDSU += 1

# print(SDSU)

createBracket()