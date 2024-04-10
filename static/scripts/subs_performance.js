function showSubType(playerType, buttonType) {
    // Cacher tous les types de joueurs
    document.querySelectorAll('.sub-content-section').forEach(function(section) {
        section.style.display = 'none';
    });
    document.querySelectorAll('.sub-perf-button').forEach(function(section) {
        section.style.backgroundColor = '#00723f';
    });
    document.getElementById(buttonType).style.backgroundColor = '#003821';
    document.getElementById(playerType).style.display = 'flex';

    if (playerType === 'sub-attackers') {
        document.getElementById('sub-attackers-matchs').style.display = 'flex';
        document.getElementById('sub-att-matchs-button').style.backgroundColor = '#003821'; // couleur de sélection
        document.getElementById('sub-attackers-global').style.display = 'none';
        document.getElementById('sub-mid-matchs-button').style.backgroundColor = '#00723f'; // couleur de non-sélection
        document.getElementById('sub-def-matchs-button').style.backgroundColor = '#00723f';
    } else if (playerType === 'sub-mid') {
        document.getElementById('sub-mid-matchs').style.display = 'flex';
        document.getElementById('sub-mid-matchs-button').style.backgroundColor = '#003821'; // couleur de sélection
        document.getElementById('sub-mid-global').style.display = 'none';
        document.getElementById('sub-att-matchs-button').style.backgroundColor = '#00723f'; // couleur de non-sélection
        document.getElementById('sub-def-matchs-button').style.backgroundColor = '#00723f';
    } else {
        document.getElementById('sub-defenders-matchs').style.display = 'flex';
        document.getElementById('sub-def-matchs-button').style.backgroundColor = '#003821'; // couleur de sélection
        document.getElementById('sub-defenders-global').style.display = 'none';
        document.getElementById('sub-att-matchs-button').style.backgroundColor = '#00723f'; // couleur de non-sélection
        document.getElementById('sub-mid-matchs-button').style.backgroundColor = '#00723f';
    }
}

function showContentSub(graphId) {
    // Cacher tous les graphiques
    document.querySelectorAll('.sub-graph-section').forEach(function(section) {
        section.style.display = 'none';
    });
    document.getElementById(graphId).style.display = 'flex';

    if (graphId === 'sub-attackers-matchs' || graphId === 'sub-mid-matchs' || graphId === 'sub-defenders-matchs') {
        document.getElementById('sub-att-matchs-button').style.backgroundColor = '#003821'; // couleur de sélection
        document.getElementById('sub-mid-matchs-button').style.backgroundColor = '#003821';
        document.getElementById('sub-def-matchs-button').style.backgroundColor = '#003821';
        document.getElementById('sub-att-global-button').style.backgroundColor = '#00723f'; // couleur de non-sélection
        document.getElementById('sub-mid-global-button').style.backgroundColor = '#00723f';
        document.getElementById('sub-def-global-button').style.backgroundColor = '#00723f';

    } else {
        document.getElementById('sub-att-matchs-button').style.backgroundColor = '#00723f'; // couleur de non-sélection
        document.getElementById('sub-mid-matchs-button').style.backgroundColor = '#00723f';
        document.getElementById('sub-def-matchs-button').style.backgroundColor = '#00723f';
        document.getElementById('sub-att-global-button').style.backgroundColor = '#003821'; // couleur de sélection
        document.getElementById('sub-mid-global-button').style.backgroundColor = '#003821';
        document.getElementById('sub-def-global-button').style.backgroundColor = '#003821';
    }
}