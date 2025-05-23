package com.expressaoregular;

/**
 *
 * @author kfrural
 */
public class ExpressaoRegular {

    //' ' (espaço), '\t' TAB, '\n' new line, '\r' volta o cursos para o inicio da linha, '\f' avanço de pagina, '\v' vertical TAB - (usado em configuraçoes de impressora)
    public String BRANCO, BRANCOS;
    public String DIGITO, DIGITOS;
    public String LETRA, LETRAS;
    public String IDENT;
    public String EXPONENCIAL;
    //public String REAL;
    public String INTEIRO;
    public String NUMEROS;
    public String ATRIBUICAO;    
    public String TRES_OU_MAIS;
    public String PALAVRA_AA_BB;
    public String REAL;
    

    /**
     * *****************************************
     * Trabalho 02
     *
     * Faças as Expressoes Regulares para reconhecer: 1. Assinatura de funções
     * ex: void funcao1(int a, float b) ex: String funcao2()
     *
     * 2. Parametros de funções ex: int a, float b ex: float media, String nome
     *
     * 3. Condicional ex: if(ano < 1990) ex: if(3*a != 4+t)
     *
     * 4. Expressão matemática ex: 3+media/3 ex: -4+beta*media[1].x ex: soma(a,
     * b)/4*vetor[5].idade
     *
     * OBS_1: Muitos erros ocorrem por falta de parenteses em torno da
     * expressão, logo use e abuse dos parenteses, eles nunca serão demais.
     *
     * OBS_2: A cada nova Expressao Regualar feita, teste-a.
     * ******************************************
     */
    public ExpressaoRegular() {
        //' ' (espaço), '\t' TAB, '\n' new line, '\r' volta o cursos para o inicio da linha, '\f' avanço de pagina, '\v' vertical TAB - (usado em configuraçoes de impressora)
        //BRANCO = "(\\s)"; // [ \t\n\r\f\v] onde
        //BRANCOS = BRANCO + "*";
        //DIGITO = "([0-9])";
        //DIGITOS = DIGITO + "*";
        //LETRA = "([A-Za-z])";
        //LETRAS = LETRA + "*";
        //IDENT = "(" + LETRA + "(" + LETRA + "|" + DIGITO + ")*)";
        //EXPONENCIAL = "(E(\\+|-)" + DIGITOS + ")";
        //REAL = "(\\-?" + DIGITOS + "\\.?" + DIGITOS + EXPONENCIAL+")";
        //INTEIRO = "("+DIGITOS + EXPONENCIAL + "?)";
        //NUMEROS = "(" + INTEIRO + "|" + REAL + ")";
        TRES_OU_MAIS = "(0|1)(0|1)(0|1)+";
        PALAVRA_AA_BB = "(a|b)*(aa|bb)+(a|b)";
        REAL = "(\\-?|[+]?)(\\d+\\.?\\d*|\\.\\d+)([eE][+-]?\\d+)?";

        //ATRIBUICAO = IDENT + BRANCOS + "=" + BRANCOS + REAL;
    }

    public void confere(String exp, String sentenca) {
        if ((sentenca != null) && !sentenca.isEmpty()) {
            if (sentenca.matches(exp)) {
                System.out.println("W:'" + sentenca + "'........ ACEITA!");
            } else {
                System.err.println("W:'" + sentenca + "'........ rejeitada.");
            }
        } else {
            System.err.println("Sentença vazia.");
        }
    }

}
