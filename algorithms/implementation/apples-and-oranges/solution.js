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

// Returns the counts of apples and oranges overlapping the house.
// s,t: inclusive range of house
// a, b: positions of apple and orange trees, respectively
// apples: distances of fallen apples from tree
// oranges: distances of fallen oranges from tree
function countApplesAndOranges (s, t, a, b, apples, oranges) {
  const fallenApples = apples.map(p => a + p)
  const fallenOranges = oranges.map(p => b + p)

  const result = {
    apples: 0,
    oranges: 0
  }

  for (const apple of fallenApples) {
    if (apple >= s && apple <= t) {
      result.apples += 1
    }
  }

  for (const orange of fallenOranges) {
    if (orange >= s && orange <= t) {
      result.oranges += 1
    }
  }

  return result
}

function main () {
  const [s, t] = readIntegerArray()
  const [a, b] = readIntegerArray()

  // We don't need to care about the numbers of apples and oranges.
  readLine()

  const apples = readIntegerArray()
  const oranges = readIntegerArray()

  const result = countApplesAndOranges(s, t, a, b, apples, oranges)

  // Open the output stream and write the result.
  const ws = createWriteStream(process.env.OUTPUT_PATH)

  ws.write(`${result.apples}\n`)
  ws.write(`${result.oranges}\n`)
  ws.end()
}
