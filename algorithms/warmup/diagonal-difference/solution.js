'use strict'

const { createWriteStream } = require('fs')

// Swtich stdin into flowing mode.
process.stdin.resume()
process.stdin.setEncoding('utf-8')

let input = ''
let inputIndex = 0

// Add incoming data to the input buffer.
process.stdin.on('data', chunk => {
  input += chunk
})

// When there is no more input to be read, split it into an array
// and call main().
process.stdin.on('end', () => {
  input = input.trim().split('\n').map(s => s.trim())
  main()
})

// Helper method to read the next input line from the buffer.
function readLine () {
  return input[inputIndex++]
}

// Return the sum of the array.
function diagnonalDifference (matrix) {
  let primary = 0
  let secondary = 0

  for (let i = 0; i < matrix.length; i++) {
    primary += matrix[i][i]
    secondary += matrix[i][matrix.length - i - 1]
  }

  return Math.abs(primary - secondary)
}

function main () {
  // Parse the number of rows and columns.
  const count = Number.parseInt(readLine(), 10)

  // The final matrix.
  const matrix = []

  for (let i = 0; i < count; i++) {
    matrix.push(readLine().split(' ').map(v => Number.parseInt(v, 10)))
  }

  const result = diagnonalDifference(matrix)

  // Open the output stream and write the result.
  const ws = createWriteStream(process.env.OUTPUT_PATH)

  ws.write(`${result}\n`)
  ws.end()
}
