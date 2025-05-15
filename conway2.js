
var golBox = document.getElementById('canvasWrapper');
var canvas = document.getElementById('board');
var ctx = canvas.getContext('2d');
var main_board = null;
var CELL_SIZE = 8;
var cell_probability = 0.3;
var CELL_COLOR = "#586e75";
var ready = false;

//create a renderer on page load
window.addEventListener('load', function () {
    if (document.getElementsByClassName("gol-box").length < 1) {
        return;
    }
    golBox = document.getElementById('canvasWrapper');
    canvas = document.getElementById("board");
    ctx = canvas.getContext("2d");
    //console.log(ctx);
    // run resizeWindow to check the width / height
    resizeWindow(undefined);

    // set up all the event listeners / timing
    window.addEventListener('resize', resizeWindow);
    window.setInterval(doBoardIteration, 100);
    window.requestAnimationFrame(doRenderIteration);
});

//if the window resizes, rerender
function resizeWindow(event) {
    canvas.width = golBox.clientWidth;
    canvas.height = golBox.clientHeight;
    //console.log("Done resizing");
    //console.log(canvas.width, canvas.height);
    main_board = getNewBoard(canvas.width / CELL_SIZE, canvas.height / CELL_SIZE);
}


function getNewBoard(h, w) {
    let local_board = []
    for (var i = 0; i < h; i++) {
        var row = []
        for (var j = 0; j < w; j++) {
            if (Math.random() <= cell_probability) {
                row.push(true);
            } else {
                row.push(false);
            }
        }
        local_board.push(row);
    }
    return local_board;
}

function neighborCount(brd, r, c) {
    let count = 0
    if (brd[r][c]) {
        count = -1;
    }
    for (var i = r - 1; i <= r + 1; i++) {
        for (var j = c - 1; j <= c + 1; j++) {
            let cell_i = i;
            let cell_j = j;
            if (cell_i < 0) {
                cell_i = brd.length - 1;
            }
            else if (cell_i > brd.length - 1) {
                cell_i = 0;
            }
            if (cell_j < 0) {
                cell_j = brd[cell_i].length - 1;
            }
            else if (cell_j > brd[cell_i].length - 1) {
                cell_j = 0;
            }
            if (brd[cell_i][cell_j]) {
                count++;
            }
        }
    }
    return count;
}

function generate_counts(brd) {
    let count_brd = []
    for (var i = 0; i < brd.length; i++) {
        var row = []
        for (var j = 0; j < brd[i].length; j++) {
            row.push(neighborCount(brd, i, j));
        }
        count_brd.push(row);
    }
    return count_brd;
}

function advanceBoard(brd) {
    let count_brd = generate_counts(brd);
    let new_board = []
    for (var i = 0; i < brd.length; i++) {
        new_board.push(brd[i].slice());
    }
    for (var i = 0; i < new_board.length; i++) {
        for (var j = 0; j < new_board[i].length; j++) {
            let count = count_brd[i][j];
            //console.log(count, i, j);
            if (new_board[i][j]) {
                if ((count != 2) && (count != 3)) {
                    new_board[i][j] = false;
                }
            } else {
                if (count == 3) {
                    new_board[i][j] = true;
                }
            }
        }
    }
    return new_board
}

function renderBoard(brd) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = CELL_COLOR;
    for (var i = 0; i < brd.length; i++) {
        for (var j = 0; j < brd[i].length; j++) {
            if (brd[i][j]) {
                ctx.fillRect(i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE);
            }
        }
    }
}

function doRenderIteration(timestamp) {
    /* only render a frame when there is a board reddit */
    if (ready) {
        renderBoard(main_board);
        ready = false;
    }
    window.requestAnimationFrame(doRenderIteration);
}

function doBoardIteration() {
    // update the main board
    main_board = advanceBoard(main_board);
    // mark the board as ready to render
    ready = true;
}

// menu stuff

document.getElementById('cellSize').addEventListener('input', (e) => {
    CELL_SIZE = parseInt(e.target.value);
    main_board = getNewBoard(canvas.width / CELL_SIZE, canvas.height / CELL_SIZE);
    console.log('Cell size changed to', e.target.value);
});

document.getElementById('boardHeight').addEventListener('input', (e) => {
    console.log('Board height changed to', e.target.value);
});

document.getElementById('boardWidth').addEventListener('input', (e) => {
    console.log('Board width changed to', e.target.value);
});

let isResizing = false;

resizer.addEventListener('mousedown', (e) => {
    isResizing = true;
});

window.addEventListener('mousemove', (e) => {
    if (!isResizing) return;
    const rect = golBox.getBoundingClientRect();
    const newWidth = e.clientX - rect.left;
    const newHeight = e.clientY - rect.top;

    // Update canvas size (both attributes and CSS)
    canvas.width = newWidth;
    canvas.height = newHeight;

    // Optional: redraw something
    ctx.fillStyle = "#ccc";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
});

window.addEventListener('mouseup', () => {
    isResizing = false;
});