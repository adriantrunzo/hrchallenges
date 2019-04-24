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

// Prints a staircase to the given stream.
function staircase (size, ws) {
  for (let i = 0; i < size; i++) {
    const step = '#'.repeat(i + 1).padStart(size)
    ws.write(`${step}\n`)
  }
}

function main () {
  // Parse the size of the staircase.
  const size = Number.parseInt(readLine(), 10)

  // Open the output stream.
  const ws = createWriteStream(process.env.OUTPUT_PATH)

  staircase(size, ws)
  ws.end()
}
