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

function readIntegerArray () {
  return readLine().split(' ').map(v => Number.parseInt(v, 10))
}

// Returns 'Cat A' if cat A catches the mouse first, 'Cat 'B' if cat B
// catches the mouse first, or 'Mouse C' if the mouse escapes.
// x: an integer, Cat A's position
// y: an integer, Cat B's position
// z: an integer, Mouse C's position
function catAndMouse (x, y, z) {
  const distanceAC = Math.abs(z - x)
  const distanceBC = Math.abs(z - y)

  if (distanceAC < distanceBC) {
    return 'Cat A'
  } else if (distanceAC > distanceBC) {
    return 'Cat B'
  } else {
    return 'Mouse C'
  }
}

function main () {
  // Parse the number of queries.
  const count = Number.parseInt(readLine(), 10)

  // Open the output stream.
  const ws = createWriteStream(process.env.OUTPUT_PATH)

  for (let i = 0; i < count; i++) {
    const [x, y, z] = readIntegerArray()
    const result = catAndMouse(x, y, z)

    ws.write(`${result}\n`)
  }

  ws.end()
}
