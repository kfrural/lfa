package com.expressaoregular;

/**
 *
 * @author jose
 */
public class Aula {

    public static void main(String[] args) {
        ExpressaoRegular ER = new ExpressaoRegular();

        //Teste 0, tres ou mais : TRES_OU_MAIS
        ER.confere(ER.TRES_OU_MAIS, "011");

        //Teste 1, aa bb subpalavras: PALAVRA_AA_BB
        ER.confere(ER.PALAVRA_AA_BB, "aabba");

        //Teste 3, aceitar exponencial: REAL
        ER.confere(ER.REAL, "-123.908777E+30");

        //Teste 1, expressão regular: DIGITOS
        //ER.confere(ER.DIGITOS, "000511200021");

        //Teste 2, expressão regular: DIGITOS
        //ER.confere(ER.DIGITOS, "000511200021ADAF");
        
        //Teste 3, expressão regular: LETRAS
        //ER.confere(ER.LETRAS, "ASDFEAFdafsafdsf");

        //Teste 4, expressão regular: LETRAS
        //ER.confere(ER.LETRAS, "ASDFEAFdafsafdsf4565");
                
        //Teste 5, expressão regular: IDENT (nome de variável, função e classes)
        //ER.confere(ER.IDENT, "Altura1");

        //Teste 6, expressão regular: IDENT (nome de variável, função e classes)
        //ER.confere(ER.IDENT, "1Altura");
                
        
        //Teste 7, expressão regular: REAL
        //ER.confere(ER.REAL, "123.908777E+30");
        
        //Teste 8, expressão regular: REAL
        //ER.confere(ER.REAL, "0.17E-5");
        
        //Teste 9, expressão regular: ATRIBUICAO
        //ER.confere(ER.ATRIBUICAO, "media=-123.908777E+30");
        
        //ER.confere(ER.INTEIRO, "10");              
    }
}
