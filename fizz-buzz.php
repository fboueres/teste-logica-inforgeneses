<?php

// percorrendo os números 1 a 50
for ($i = 1; $i <= 50; $i++) {
    $output = '';

    // se número for múltiplo de 3, então Fizz
    if ($i % 3 == 0)
        $output .= 'Fizz';

    // se número for múltiplo de 5, então Buzz
    if ($i % 5 == 0)
        $output .= 'Buzz';

    /**
     * se o número for tanto múltiplo de 3 e 5, então FizzBuzz
     * isso é possível por causa da string $ouput porque
     * as condições concatenam nela se verdadeiras
     */

    /**
     * a variável output será uma string vazia caso
     * nenhuma condição seja verdadeira
     * se ela for uma string vazia
     * então a saída será $i 
     */

    echo ($output ?: $i) . '<br>';
}