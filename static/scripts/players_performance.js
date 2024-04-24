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
    } else if (playerType === 'mid') {
        document.getElementById('mid-matchs').style.display = 'flex';
    } else {
        document.getElementById('defenders-matchs').style.display = 'flex';
    }
}