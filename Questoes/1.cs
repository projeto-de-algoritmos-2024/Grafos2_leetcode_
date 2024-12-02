public class Solution 
{
    // Método que retorna um array contendo os índices de dois números que somam o valor 'target'
    public int[] TwoSum(int[] nums, int target) 
    {
        // Cria um array de tamanho 2 para armazenar os índices dos números encontrados
        int[] z = new int[2];
        
        // Loop externo para iterar por todos os elementos do array
        for (int x = 0; x < nums.Length; x++) 
        {
            // Loop interno para comparar o elemento atual com todos os outros
            for (int y = 0; y < nums.Length; y++) 
            {
                // Verifica se os índices são diferentes para evitar usar o mesmo elemento duas vezes
                if (x != y) 
                {
                    // Verifica se a soma dos elementos nos índices x e y é igual ao 'target'
                    if (nums[x] + nums[y] == target) 
                    {
                        // Armazena os índices no array de resultado
                        z[0] = x;
                        z[1] = y;
                    }
                }
            }
        }
        
        // Retorna o array com os índices encontrados
        return z;
    }
}
