function showMatch(graphId) {
    // Cacher tous les graphiques
    document.querySelectorAll('.graph').forEach(function(section) {
        section.style.display = 'none';
    });
    document.getElementById(graphId).style.display = 'flex';

    // Couleur de sélection : 003821
    // Couleur de non-sélection : 00723f
    if (graphId === 'match1') {
        document.getElementById('match1-button').style.backgroundColor = '#003821';
        document.getElementById('match2-button').style.backgroundColor = '#00723f';
        document.getElementById('match3-button').style.backgroundColor = '#00723f';
        document.getElementById('match4-button').style.backgroundColor = '#00723f';
        document.getElementById('match5-button').style.backgroundColor = '#00723f';
        document.getElementById('match6-button').style.backgroundColor = '#00723f';
        document.getElementById('match7-button').style.backgroundColor = '#00723f';
    }
    if (graphId === 'match2') {
        document.getElementById('match1-button').style.backgroundColor = '#00723f';
        document.getElementById('match2-button').style.backgroundColor = '#003821';
        document.getElementById('match3-button').style.backgroundColor = '#00723f';
        document.getElementById('match4-button').style.backgroundColor = '#00723f';
        document.getElementById('match5-button').style.backgroundColor = '#00723f';
        document.getElementById('match6-button').style.backgroundColor = '#00723f';
        document.getElementById('match7-button').style.backgroundColor = '#00723f';
        
    }
    if (graphId === 'match3') {
        document.getElementById('match1-button').style.backgroundColor = '#00723f';
        document.getElementById('match2-button').style.backgroundColor = '#00723f';
        document.getElementById('match3-button').style.backgroundColor = '#003821';
        document.getElementById('match4-button').style.backgroundColor = '#00723f';
        document.getElementById('match5-button').style.backgroundColor = '#00723f';
        document.getElementById('match6-button').style.backgroundColor = '#00723f';
        document.getElementById('match7-button').style.backgroundColor = '#00723f';
    }
    if (graphId === 'match4') {
        document.getElementById('match1-button').style.backgroundColor = '#00723f';
        document.getElementById('match2-button').style.backgroundColor = '#00723f';
        document.getElementById('match3-button').style.backgroundColor = '#00723f';
        document.getElementById('match4-button').style.backgroundColor = '#003821';
        document.getElementById('match5-button').style.backgroundColor = '#00723f';
        document.getElementById('match6-button').style.backgroundColor = '#00723f';
        document.getElementById('match7-button').style.backgroundColor = '#00723f';
    }
    if (graphId === 'match5') {
        document.getElementById('match1-button').style.backgroundColor = '#00723f';
        document.getElementById('match2-button').style.backgroundColor = '#00723f';
        document.getElementById('match3-button').style.backgroundColor = '#00723f';
        document.getElementById('match4-button').style.backgroundColor = '#00723f';
        document.getElementById('match5-button').style.backgroundColor = '#003821';
        document.getElementById('match6-button').style.backgroundColor = '#00723f';
        document.getElementById('match7-button').style.backgroundColor = '#00723f';
    }
    if (graphId === 'match6') {
        document.getElementById('match1-button').style.backgroundColor = '#00723f';
        document.getElementById('match2-button').style.backgroundColor = '#00723f';
        document.getElementById('match3-button').style.backgroundColor = '#00723f';
        document.getElementById('match4-button').style.backgroundColor = '#00723f';
        document.getElementById('match5-button').style.backgroundColor = '#00723f';
        document.getElementById('match6-button').style.backgroundColor = '#003821';
        document.getElementById('match7-button').style.backgroundColor = '#00723f';
    }
    if (graphId === 'match7') {
        document.getElementById('match1-button').style.backgroundColor = '#00723f';
        document.getElementById('match2-button').style.backgroundColor = '#00723f';
        document.getElementById('match3-button').style.backgroundColor = '#00723f';
        document.getElementById('match4-button').style.backgroundColor = '#00723f';
        document.getElementById('match5-button').style.backgroundColor = '#00723f';
        document.getElementById('match6-button').style.backgroundColor = '#00723f';
        document.getElementById('match7-button').style.backgroundColor = '#003821';
    }
}