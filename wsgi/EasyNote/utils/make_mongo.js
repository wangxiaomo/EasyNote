var db = connect('EasyNote');
db.notes.save({text:'This is My First Note', date:(new Date()).toLocaleString()})
db.notes.save({text:'This is My Second Note', date:(new Date()).toLocaleString()})
db.notes.save({text:'This is My Third Note', date:(new Date()).toLocaleString()})
db.notes.save({text:'This is My Firth Note', date:(new Date()).toLocaleString()})
db.notes.save({text:'This is My Fifth Note', date:(new Date()).toLocaleString()})
