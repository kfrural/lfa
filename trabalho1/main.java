// teste codguin simples so pra ter ideia do trampo, falta serializador e altear entradas, so testando a matriz mesmo
import java.io.*;
import java.util.*;

public class Main {
    private static int[][] matrizTransicao;
    private static boolean[] estadosFinais;
    private static String alfabeto = "ab";
    
    public static void main(String[] args) {
        matrizTransicao = new int[][]{
            {1, 2},  // q0: a->q1, b->q2
            {3, 2},  // q1: a->qf, b->q2
            {1, 3},  // q2: a->q1, b->qf
            {3, 3}   // qf: a->qf, b->qf
        };
        
        estadosFinais = new boolean[]{false, false, false, true};
        
        System.out.println("Testando palavras:");
        System.out.println("abba: " + reconhecer("abba"));
        System.out.println("aba: " + reconhecer("aba"));
        
        Scanner scanner = new Scanner(System.in);
        System.out.println("\nDigite uma palavra para testar (ou 'sair' para encerrar):");
        
        while (true) {
            String palavra = scanner.nextLine();
            if (palavra.equalsIgnoreCase("sair")) {
                break;
            }
            System.out.println("Resultado: " + reconhecer(palavra));
        }
        
        scanner.close();
    }
    
    private static boolean reconhecer(String palavra) {
        int estadoAtual = 0;
        
        for (char c : palavra.toCharArray()) {
            int indiceSimbolo = alfabeto.indexOf(c);
            
            if (indiceSimbolo == -1) {
                return false;
            }
            
            estadoAtual = matrizTransicao[estadoAtual][indiceSimbolo];
        }
        
        return estadosFinais[estadoAtual];
    }
}
