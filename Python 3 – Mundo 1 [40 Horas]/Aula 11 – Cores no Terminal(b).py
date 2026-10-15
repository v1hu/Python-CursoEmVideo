# Cores ANSI no Python

# Estilos
print('\n\033[1mESTILOS\033[m')
print('\033[0m0 - Normal\033[m')
print('\033[1m1 - Negrito\033[m')
print('\033[2m2 - Transparente/Fraco\033[m')
print('\033[3m3 - Itálico\033[m')
print('\033[4m4 - Sublinhado\033[m')
print('\033[7m7 - Invertido\033[m')
print('\033[9m9 - Tachado\033[m')

# Cores do texto
print('\n\033[1mCORES DO TEXTO\033[m')
print('\033[30m30 - Preto\033[m')
print('\033[31m31 - Vermelho\033[m')
print('\033[32m32 - Verde\033[m')
print('\033[33m33 - Amarelo\033[m')
print('\033[34m34 - Azul\033[m')
print('\033[35m35 - Magenta/Roxo\033[m')
print('\033[36m36 - Ciano\033[m')
print('\033[37m37 - Branco\033[m')
print('\033[90m90 - Cinza\033[m')
print('\033[97m97 - Branco brilhante\033[m')

# Cores do fundo
print('\n\033[1mCORES DO FUNDO\033[m')
print('\033[40m40 - Preto\033[m')
print('\033[41m41 - Vermelho\033[m')
print('\033[42m42 - Verde\033[m')
print('\033[43m43 - Amarelo\033[m')
print('\033[44m44 - Azul\033[m')
print('\033[45m45 - Magenta/Roxo\033[m')
print('\033[46m46 - Ciano\033[m')
print('\033[47m47 - Branco\033[m')
print('\033[100m100 - Cinza brilhante\033[m')
print('\033[107m107 - Branco brilhante\033[m')

# Combinações
print('\n\033[1mCOMBINAÇÕES\033[m')
print('\033[1;31;40mNegrito + texto vermelho + fundo preto\033[m')
print('\033[4;33;44mSublinhado + texto amarelo + fundo azul\033[m')
print('\033[7;97;41mInvertido + texto branco + fundo vermelho\033[m')
print('\033[1;32;43mNegrito + texto verde + fundo amarelo\033[m')

''''
╔══════════════════════════════════════════════════════════╗
║                  GUIA DE CORES ANSI                      ║
║                     PYTHON                               ║
╚══════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. ESTILOS DE TEXTO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0  = Normal / Reset
1  = Negrito
2  = Fraco
3  = Itálico
4  = Sublinhado
7  = Texto invertido
9  = Tachado

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. CORES DO TEXTO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

30 = Preto
31 = Vermelho
32 = Verde
33 = Amarelo
34 = Azul
35 = Magenta / Roxo
36 = Ciano
37 = Branco

90 = Cinza brilhante
91 = Vermelho brilhante
92 = Verde brilhante
93 = Amarelo brilhante
94 = Azul brilhante
95 = Magenta brilhante
96 = Ciano brilhante
97 = Branco brilhante

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. CORES DO FUNDO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

40 = Preto
41 = Vermelho
42 = Verde
43 = Amarelo
44 = Azul
45 = Magenta / Roxo
46 = Ciano
47 = Branco

100 = Cinza brilhante
101 = Vermelho brilhante
102 = Verde brilhante
103 = Amarelo brilhante
104 = Azul brilhante
105 = Magenta brilhante
106 = Ciano brilhante
107 = Branco brilhante

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. COMO UTILIZAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ESTRUTURA:
\033[ESTILO;COR_DO_TEXTO;COR_DO_FUNDOm

EXEMPLO:
print('\033[1;97;42mOlá, Mundo!\033[m')

1  = Negrito
97 = Branco brilhante
42 = Fundo verde

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5. REGRAS IMPORTANTES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• \033[ inicia a sequência ANSI.
• Os códigos são separados por ponto e vírgula (;).
• A letra m encerra os parâmetros de formatação.
• \033[m reseta a formatação ao padrão do terminal.
• Você pode combinar estilos, cores de texto e fundos.
• O resultado depende do terminal e de suas configurações.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                 BONS ESTUDOS EM PYTHON!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
'''