<?php

// número iniciais da sequência de fibonacci
$nums = [0, 1];

// percorrendo os primeiros 40 números da sequência de fibonacci
for ($i = 1; $i <= 40; $i++) {
    //calcula o número seguinte da sequência
    $next = $nums[0] + $nums[1];

    // externa o número na saída
    echo $nums[0] . ($i == 40 ?: ', ');
    
    /**
     * inverte o array com os números anteriores 
     * para o cálculo do número seguinte
     * assim se tem os últimos números
     * a serem usadas para soma do próximo
     */
    $nums = array_reverse($nums);
    $nums[1] = $next;
}