public enum TipoToken {
    // Tokens de un sólo caracter
    LEFT_PAREN, RIGHT_PAREN, COMMA, SEMICOLON,
    MINUS, PLUS, SLASH, STAR, MOD,

    // Tokens de uno o dos caracteres
    BANG, BANG_EQUAL,
    EQUAL, EQUAL_EQUAL,
    GREATER, GREATER_EQUAL,
    LESS, LESS_EQUAL,

    // Literales
    IDENTIFIER, NUMBER,

    EOF
}
