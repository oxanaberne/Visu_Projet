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
    } else if (playerType === 'sub-mid') {
        document.getElementById('sub-mid-matchs').style.display = 'flex';
    } else {
        document.getElementById('sub-defenders-matchs').style.display = 'flex';
    }
}