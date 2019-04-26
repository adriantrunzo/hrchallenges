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

// Returns an array of rounded grades.
function gradingStudents (grades) {
  const rounded = []

  for (let grade of grades) {
    if (grade >= 38) {
      const difference = (5 - (grade % 5))

      if (difference < 3) {
        grade += difference
      }
    }

    rounded.push(grade)
  }

  return rounded
}

function main () {
  // Parse the number of grades.
  const count = Number.parseInt(readLine(), 10)

  // The final matrix.
  const grades = []

  for (let i = 0; i < count; i++) {
    grades.push(Number.parseInt(readLine(), 10))
  }

  const result = gradingStudents(grades)

  // Open the output stream and write the result.
  const ws = createWriteStream(process.env.OUTPUT_PATH)

  ws.write(`${result.join('\n')}\n`)
  ws.end()
}
