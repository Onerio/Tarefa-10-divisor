#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  divisor.py
#  
#  Copyright 2018 20181bsi0121 <20181bsi0121@SR6192>
#  
# 

def main():
    
    cont = 1;
    
    while cont <= 2:

        num1 = 0; num2 = 0; num3 = 0;
        max_divisor1 = 1;
        resto = 0;
        num1 = int(input("Digite o primeiro número: "));
        #num2 = int(input("Digite o segundo número: "));    
        #num3 = int(input("Digite o terceiro número: "));

        while max_divisor1 <= num1:
            
            resto = num1 % max_divisor1; 
            if resto==0:
                print(max_divisor1)
            
            max_divisor1 = max_divisor1 + 1;

        print('Nº 1',num1,' Max divisor: ',max_divisor1)
        #print('Nº 2',num2,' Max divisor: ',max_divisor2)
        #print('Nº 3',num3,' Max divisor: ',max_divisor3)

        cont = cont + 1

   
    return 0

if __name__ == '__main__':
	main()
