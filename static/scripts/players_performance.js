function showPlayerType(playerType, buttonType) {
    // Cacher tous les types de joueurs
    document.querySelectorAll('.content-section').forEach(function(section) {
        section.style.display = 'none';
    });
    document.querySelectorAll('.perf-button').forEach(function(section) {
        section.style.backgroundColor = '#00723f';
    });
    document.getElementById(buttonType).style.backgroundColor = '#003821';
    document.getElementById(playerType).style.display = 'flex';

    if (playerType === 'attackers') {
        document.getElementById('attackers-matchs').style.display = 'flex';
        document.getElementById('att-matchs-button').style.backgroundColor = '#003821'; // couleur de sélection
        document.getElementById('attackers-global').style.display = 'none';
        document.getElementById('mid-matchs-button').style.backgroundColor = '#00723f'; // couleur de non-sélection
        document.getElementById('def-matchs-button').style.backgroundColor = '#00723f';
    } else if (playerType === 'mid') {
        document.getElementById('mid-matchs').style.display = 'flex';
        document.getElementById('mid-matchs-button').style.backgroundColor = '#003821'; // couleur de sélection
        document.getElementById('mid-global').style.display = 'none';
        document.getElementById('att-matchs-button').style.backgroundColor = '#00723f'; // couleur de non-sélection
        document.getElementById('def-matchs-button').style.backgroundColor = '#00723f';
    } else {
        document.getElementById('defenders-matchs').style.display = 'flex';
        document.getElementById('def-matchs-button').style.backgroundColor = '#003821'; // couleur de sélection
        document.getElementById('defenders-global').style.display = 'none';
        document.getElementById('att-matchs-button').style.backgroundColor = '#00723f'; // couleur de non-sélection
        document.getElementById('mid-matchs-button').style.backgroundColor = '#00723f';
    }
}

function showContent(graphId) {
    // Cacher tous les graphiques
    document.querySelectorAll('.graph-section').forEach(function(section) {
        section.style.display = 'none';
    });
    document.getElementById(graphId).style.display = 'flex';

    if (graphId === 'attackers-matchs' || graphId === 'mid-matchs' || graphId === 'defenders-matchs') {
        document.getElementById('att-matchs-button').style.backgroundColor = '#003821'; // couleur de sélection
        document.getElementById('mid-matchs-button').style.backgroundColor = '#003821';
        document.getElementById('def-matchs-button').style.backgroundColor = '#003821';
        document.getElementById('att-global-button').style.backgroundColor = '#00723f'; // couleur de non-sélection
        document.getElementById('mid-global-button').style.backgroundColor = '#00723f';
        document.getElementById('def-global-button').style.backgroundColor = '#00723f';

    } else {
        document.getElementById('att-matchs-button').style.backgroundColor = '#00723f'; // couleur de non-sélection
        document.getElementById('mid-matchs-button').style.backgroundColor = '#00723f';
        document.getElementById('def-matchs-button').style.backgroundColor = '#00723f';
        document.getElementById('att-global-button').style.backgroundColor = '#003821'; // couleur de sélection
        document.getElementById('mid-global-button').style.backgroundColor = '#003821';
        document.getElementById('def-global-button').style.backgroundColor = '#003821';
    }
}