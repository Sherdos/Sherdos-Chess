

function move() {
    fetch('move/')
    .then(function(response) {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Ошибка запроса');
        }
        })
    .then(function(data) {
        create_board(data)
    })
    .catch(function(error) {
        console.log(error);
    });
}

function create_board(db_board) {
    var old = document.getElementsByClassName('board')
    var board = document.createElement('div');
    board.className = 'board';
    document.body.appendChild(board)
    
    for (let db_line of db_board){
        var line = document.createElement('div');
        line.className = 'line';
        board.appendChild(line);
        for (let db_cell of db_line){
            var cell = document.createElement('div')
            cell.className = 'cell bg-'+db_cell['color'];
            cell.id=String(db_cell['x'])+String(db_cell['y'])
            line.appendChild(cell);
            if (db_cell['figure'] !== null && db_cell['figure'] !== undefined){
                figure_image = document.createElement('img');
                figure_image.src='/static/game/images/'+db_cell['figure']+'.png';
                figure_image.className = 'figure-image'
                cell.appendChild(figure_image);
            }
        }
    }
}

