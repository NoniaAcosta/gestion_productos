// 1. Qué son los Arrays
// 1.1 Crea una función llamada `procesarPedido` que recibe un array `pedido`.
// Debes sacar el primer elemento (nombre del cliente), añadir "bebida" al inicio del array y añadir el nombre del cliente al final.
let miPedido = ["Nonia Acosta", "bebida"];
procesarPedido(miPedido);
function procesarPedido(pedido) {
    nombre_cli=pedido.shift();
    pedido.push(nombre_cli);
    return pedido;
}

// 2. Iteración de Arrays en Javascript
// 2.1 Crea una función llamada `sumarPares` que reciba un array de números.
// Debes iterar sobre el array, sumar todos los números pares y devolver la suma.
let misNumeros = [2, 5, 6, 7, 8, 9, 10];
sumarPares(misNumeros);
function sumarPares(numeros) {
    let suma = 0;
    let i = 0;
    while (i < numeros.length) {
        if (numeros[i] % 2 === 0) {
            suma = suma + numeros[i];
        }
        i++;
    }
    return suma;
}

// 3. Buscar en Arrays
// 3.1 Escribe una función llamada `palabrasTerminanConA` que reciba un array de palabras y devuelva `true` si todas terminan con "a", o `false` si al menos una no lo hace.
function palabrasTerminanConA(palabras) {
    const encontrados = palabras.every(palabra => palabra.endsWith('a'));
    return encontrados;
}

const palabras = ['casa', 'silla', 'mesa']
console.log(palabrasTerminanConA(palabras)) // -> true

// 4. Transformar Arrays
// 4.1 Crea una función llamada `buscaPalabras` que reciba dos parámetros: un array `words` y una palabra `word`.
// Busca el índice de la palabra en el array y devuelve todas las palabras después de ese índice en un nuevo array
function buscaPalabras(words, word) {
    const indice = words.indexOf(word);
    return words.slice(indice + 1, words.length);
}

const words = ['hola', 'mundo', 'javascript', 'node'];
console.log(buscaPalabras(words, 'mundo')) // El resultado debe ser: ['javascript', 'node']

// 5. Matrices
// 5.1 Crea una función llamada `findJavaScript` que reciba una matriz de cadenas y devuelva la posición de "JavaScript".
// Si no la encuentra, devuelve [-1, -1].
function findJavaScript(matrix) {
    for (let fila = 0; fila < matrix.length; fila++) {
        for (let columna = 0; columna < matrix.length; columna++) {
            const indice = matrix[fila][columna].indexOf("JavaScript");
            if (indice !== -1) {
                return [fila, columna]
            }
        }
    }
    return [-1, -1];
}

const matrix = [
    ['HTML', 'CSS', 'JavaScript'],
    ['Java', 'C++', 'Python'],
    ['Ruby', 'Go', 'Swift']
]

const position = findJavaScript(matrix);
console.log(position); // -> [0, 2]

// 6. Algoritmos con Arrays
// 6.1 Crea una función llamada `findMinMaxPages` que reciba un array de números (representando el número de páginas de libros).
// La función debe devolver un array con dos posiciones: el índice del libro con menos páginas y el índice del libro con más páginas.
function findMinMaxPages(books) {
    for (let fila = 0; fila < books.length; fila++) {
        if (fila === 0) {
            mayor = books[fila];
            menor = books[fila];
            posicionMayor=fila;
            posicionMenor=fila;
        } else if (books[fila] > mayor) {
            mayor = books[fila]
            posicionMayor=fila;
        } else if (books[fila] < menor) {
            menor = books[fila]
            posicionMenor=fila;
        }
    }
    return [posicionMenor, posicionMayor]
}

const libros = [350, 120, 540, 275, 390, 130, 670];
const resultado = findMinMaxPages(libros);
console.log(resultado); // -> [1, 6]

// Exportar las funciones para que puedan ser completadas y probadas
module.exports = {
    procesarPedido,
    sumarPares,
    palabrasTerminanConA,
    buscaPalabras,
    findJavaScript,
    findMinMaxPages
};
