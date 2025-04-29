import java.io.*;
import java.util.*;

public class Main {
    private static class Automato {
        private final int[][] matrizTransicao;
        private final int estadoFinal;
        private final String alfabeto;

        public Automato(int[][] matrizTransicao, int estadoFinal, String alfabeto) {
            this.matrizTransicao = matrizTransicao;
            this.estadoFinal = estadoFinal;
            this.alfabeto = alfabeto;
        }

        public boolean reconhecer(String palavra) {
            int estadoAtual = 0;
            
            for (char c : palavra.toCharArray()) {
                int indiceSimbolo = alfabeto.indexOf(c);
                
                if (indiceSimbolo == -1) {
                    return false;
                }
                
                estadoAtual = matrizTransicao[estadoAtual][indiceSimbolo];
            }
            
            return estadoAtual == estadoFinal;
        }
    }

    private static Automato lerAutomatoDeArquivo(String caminhoArquivo) throws IOException {
        try (BufferedReader leitor = new BufferedReader(new FileReader(caminhoArquivo))) {
            int numEstados = Integer.parseInt(leitor.readLine().trim());
            
            String alfabeto = leitor.readLine().trim();
            
            int estadoFinal = Integer.parseInt(leitor.readLine().trim());
            
            List<int[]> linhas = new ArrayList<>();
            String linha;
            while ((linha = leitor.readLine()) != null) {
                String[] estados = linha.trim().split(";");
                if (estados.length == 2) {
                    linhas.add(new int[] {
                        Integer.parseInt(estados[0]),
                        Integer.parseInt(estados[1])
                    });
                }
            }
            
            int[][] matrizTransicao = new int[linhas.size()][alfabeto.length()];
            for (int i = 0; i < linhas.size(); i++) {
                matrizTransicao[i] = new int[alfabeto.length()];
                matrizTransicao[i][0] = linhas.get(i)[0];
                matrizTransicao[i][1] = linhas.get(i)[1];
            }
            
            return new Automato(matrizTransicao, estadoFinal, alfabeto);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        try {
            String caminho = "automato.csv";
            Automato automato = lerAutomatoDeArquivo(caminho);
        
            System.out.println("\nDigite palavras para testar (ou 'sair' para encerrar):");
            while (true) {
                String palavra = scanner.nextLine();
                if (palavra.equalsIgnoreCase("sair")) {
                    break;
                }
                boolean resultado = automato.reconhecer(palavra);
                System.out.println("Resultado: " + resultado);
            }
        } catch (IOException e) {
            System.err.println("Erro ao ler o arquivo: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }
}
