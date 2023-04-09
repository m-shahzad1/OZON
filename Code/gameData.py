from pathlib import Path

# Default Size
size = (1000,600)
# Default Resolution
res = (44,20)
# Player Size
player_size = (2,2)

#Berry Size 
berry_size = (1,1)

#Enemy Size 
enemy_size = (2,2)

#Boss Size
boss_size = (5,10)

# Game Settings:

# Default Health
health = 100
# Default Velo
velo = 15
# Default JumpHeight
jump_height = 100
#Default damage
damage = 10

level1 = {
    'platforms' : [f.split(' ') for f in [a for a in open(Path('Code/levels/level1/platforms.txt')).read().split('\n')]],
    'berries'   : [f.split(' ') for f in [a for a in open(Path('Code/levels/level1/berries.txt')).read().split('\n')]],
    'enemy'     : [f.split(' ') for f in [a for a in open(Path('Code/levels/level1/enemies.txt')).read().split('\n')]],
    'boss'      : [a for a in open(Path('Code/levels/level1/boss.txt')).read().split(' ')],
    'player' : (3,3),
    'stretch' : 4,
    'map' : Path(r'Code/Assets/backgroundImages/SouthAmericaLevel1.png')
}
level2 = {
    'platforms' : [f.split(' ') for f in [a for a in open(Path('Code/levels/level2/platforms.txt')).read().split('\n')]],
    'berries'   : [f.split(' ') for f in [a for a in open(Path('Code/levels/level2/berries.txt')).read().split('\n')]],
    'enemy'     : [f.split(' ') for f in [a for a in open(Path('Code/levels/level2/enemies.txt')).read().split('\n')]],
    'boss'      : [a for a in open(Path('Code/levels/level2/boss.txt')).read().split(' ')],
    'player' : (3,3),
    'stretch' : 4,
    'map' : Path(r'Code/Assets/backgroundImages/SouthAmericaLevel2.png')
}
level3 = {
    'platforms' : [f.split(' ') for f in [a for a in open(Path('Code/levels/level3/platforms.txt')).read().split('\n')]],
    'berries'   : [f.split(' ') for f in [a for a in open(Path('Code/levels/level3/berries.txt')).read().split('\n')]],
    'enemy'     : [f.split(' ') for f in [a for a in open(Path('Code/levels/level3/enemies.txt')).read().split('\n')]],
    'boss'      : [a for a in open(Path('Code/levels/level3/boss.txt')).read().split(' ')],
    'player' : (3,3),
    'stretch' : 4,
    'map' : Path(r'Code/Assets/backgroundImages/NorthAmericaLevel3.png')
}

level4={
    'platforms' : [f.split(' ') for f in [a for a in open(Path('Code/levels/level4/platforms.txt')).read().split('\n')]],
    'berries'   : [f.split(' ') for f in [a for a in open(Path('Code/levels/level4/berries.txt')).read().split('\n')]],
    'enemy'     : [f.split(' ') for f in [a for a in open(Path('Code/levels/level4/enemies.txt')).read().split('\n')]],
    'boss'      : [a for a in open(Path('Code/levels/level4/boss.txt')).read().split(' ')],
    'player' : (3,3),
    'stretch' : 4,
    'map' : Path(r'Code/Assets/backgroundImages/NorthAmericaLevel4.png')
}
level5={
    'platforms' : [f.split(' ') for f in [a for a in open(Path('Code/levels/level5/platforms.txt')).read().split('\n')]],
    'berries'   : [f.split(' ') for f in [a for a in open(Path('Code/levels/level5/berries.txt')).read().split('\n')]],
    'enemy'     : [f.split(' ') for f in [a for a in open(Path('Code/levels/level5/enemies.txt')).read().split('\n')]],
    'boss'      : [a for a in open(Path('Code/levels/level5/boss.txt')).read().split(' ')],
    'player' : (3,3),
    'stretch' : 4,
    'map' : Path(r'Code/Assets/backgroundImages/EuropeLevel5.png')
}
level6={
    'platforms' : [f.split(' ') for f in [a for a in open(Path('Code/levels/level6/platforms.txt')).read().split('\n')]],
    'berries'   : [f.split(' ') for f in [a for a in open(Path('Code/levels/level6/berries.txt')).read().split('\n')]],
    'enemy'     : [f.split(' ') for f in [a for a in open(Path('Code/levels/level6/enemies.txt')).read().split('\n')]],
    'boss'      : [a for a in open(Path('Code/levels/level6/boss.txt')).read().split(' ')],
    'player' : (3,3),
    'stretch' : 4,
    'map' : Path(r'Code/Assets/backgroundImages/ArabiaLevel6.png')
}
level7={
    'platforms' : [f.split(' ') for f in [a for a in open(Path('Code/levels/level7/platforms.txt')).read().split('\n')]],
    'berries'   : [f.split(' ') for f in [a for a in open(Path('Code/levels/level7/berries.txt')).read().split('\n')]],
    'enemy'     : [f.split(' ') for f in [a for a in open(Path('Code/levels/level7/enemies.txt')).read().split('\n')]],
    'boss'      : [a for a in open(Path('Code/levels/level7/boss.txt')).read().split(' ')],
    'player' : (3,3),
    'stretch' : 4,
    'map' : Path(r'Code/Assets/backgroundImages/AfricaLevel7.png')
}

makerLevel={
    'platforms' : [f.split(' ') for f in [a for a in open(Path('Code/levels/makerLevel/platforms.txt')).read().split('\n')]],
    'berries'   : [f.split(' ') for f in [a for a in open(Path('Code/levels/makerLevel/berries.txt')).read().split('\n')]],
    'enemy'     : [f.split(' ') for f in [a for a in open(Path('Code/levels/makerLevel/enemies.txt')).read().split('\n')]],
    'boss'      : [a for a in open(Path('Code/levels/makerLevel/boss.txt')).read().split(' ')],
    'player' : (3,3),
    'stretch' : 4,
    'map' : Path(r'Code/sprites/levels/level1/levelBack.png')
}

miniLevel = {
    'platforms' : [f.split(' ') for f in [a for a in open(Path('Code/levels/miniLevel/platforms.txt')).read().split('\n')]],
    'berries'   : [f.split(' ') for f in [a for a in open(Path('Code/levels/miniLevel/berries.txt')).read().split('\n')]],
    'enemy'     : [f.split(' ') for f in [a for a in open(Path('Code/levels/miniLevel/enemies.txt')).read().split('\n')]],
    'boss'      : [a for a in open(Path('Code/levels/miniLevel/boss.txt')).read().split(' ')],
    'player' : (3,3),
    'stretch' : 1,
    'map' : Path(r'Code/sprites/levels/level1/levelBack.png')
}

levels = [level1,level2,level3,level4,level5,level6,level7,makerLevel,miniLevel]

map1 = {
    'background' : Path(r'Code/sprites/map/mapLevel0passed.png'),
    'playerSpawn' : 0,
}
map2 = {
    'background' : Path(r'Code/sprites/map/mapLevel1passed.png'),
    'playerSpawn' : 0,
}
map3 = {
    'background' : Path(r'Code/sprites/map/mapLevel2passed.png'),
    'playerSpawn' : 0,
}
map4 = {
    'background' : Path(r'Code/sprites/map/mapLevel3passed.png'),
    'playerSpawn' : 0,
}
map5 = {
    'background' : Path(r'Code/sprites/map/mapLevel4passed.png'),
    'playerSpawn' : 0,
}
map6 = {
    'background' : Path(r'Code/sprites/map/mapLevel5passed.png'),
    'playerSpawn' : 0,
}
map7 = {
    'background' : Path(r'Code/sprites/map/mapLevel6passed.png'),
    'playerSpawn' : 0,
}
map8 = {
    'background' : Path(r'Code/sprites/map/mapLevel6passed.png'),
    'playerSpawn' : 0,
}
maps = [map1,map2,map3,map4,map5,map6,map7,map8]
map_unlock = [a for a in open(Path('Code/data/master.txt')).read().split(' ')][1]
path_overWorld = Path('Code/path/path_overworld.json')

ozonBlue = {
    'sprite' : {'walkRight' : [Path(r'Code/sprites/player/ozonBlue/wr1.png'), Path(r'Code/sprites/player/ozonBlue/wr2.png'), Path(r'Code/sprites/player/ozonBlue/wr3.png'), Path(r'Code/sprites/player/ozonBlue/wr4.png'), Path(r'Code/sprites/player/ozonBlue/wr5.png')],
                'walkLeft' : [Path(r'Code/sprites/player/ozonBlue/wl1.png'), Path(r'Code/sprites/player/ozonBlue/wl2.png'), Path(r'Code/sprites/player/ozonBlue/wl3.png'), Path(r'Code/sprites/player/ozonBlue/wl4.png'), Path(r'Code/sprites/player/ozonBlue/wl5.png')],
                'lookRight' : [Path(r'Code/sprites/player/ozonBlue/sr.png')],
                'lookLeft' : [Path(r'Code/sprites/player/ozonBlue/sl.png')],
                'jumpRight' : [Path(r'Code/sprites/player/ozonBlue/jr.png')],
                'jumpLeft' : [Path(r'Code/sprites/player/ozonBlue/jl.png')]
                },
    'vel' : velo*1.2,
    'maxJumpHeight' : jump_height,
    'health' : health
}
ozonGreen = {
    'sprite' : {'walkRight' : [Path(r'Code/sprites/player/ozonGreen/gwr1.png'), Path(r'Code/sprites/player/ozonGreen/gwr2.png'), Path(r'Code/sprites/player/ozonGreen/gwr3.png'), Path(r'Code/sprites/player/ozonGreen/gwr4.png'), Path(r'Code/sprites/player/ozonGreen/gwr5.png')],
                'walkLeft' : [Path(r'Code/sprites/player/ozonGreen/gwl1.png'), Path(r'Code/sprites/player/ozonGreen/gwl2.png'), Path(r'Code/sprites/player/ozonGreen/gwl3.png'), Path(r'Code/sprites/player/ozonGreen/gwl4.png'), Path(r'Code/sprites/player/ozonGreen/gwl5.png')],
                'lookRight' : [Path(r'Code/sprites/player/ozonGreen/gsr.png')],
                'lookLeft' : [Path(r'Code/sprites/player/ozonGreen/gsl.png')],
                'jumpRight' : [Path(r'Code/sprites/player/ozonGreen/gjr.png')],
                'jumpLeft' : [Path(r'Code/sprites/player/ozonGreen/gjl.png')]
                },
    'vel' : velo,
    'maxJumpHeight' : jump_height*1.2,
    'health' : health
}
ozonRed = {
    'sprite' : {'walkRight' : [Path(r'Code/sprites/player/ozonRed/rwr1.png'), Path(r'Code/sprites/player/ozonRed/rwr2.png'), Path(r'Code/sprites/player/ozonRed/rwr3.png'), Path(r'Code/sprites/player/ozonRed/rwr4.png'), Path(r'Code/sprites/player/ozonRed/rwr5.png')],
                'walkLeft' : [Path(r'Code/sprites/player/ozonRed/rwl1.png'), Path(r'Code/sprites/player/ozonRed/rwl2.png'), Path(r'Code/sprites/player/ozonRed/rwl3.png'), Path(r'Code/sprites/player/ozonRed/rwl4.png'), Path(r'Code/sprites/player/ozonRed/rwl5.png')],
                'lookRight' : [Path(r'Code/sprites/player/ozonRed/rsr.png')],
                'lookLeft' : [Path(r'Code/sprites/player/ozonRed/rsl.png')],
                'jumpRight' : [Path(r'Code/sprites/player/ozonRed/rjr.png')],
                'jumpLeft' : [Path(r'Code/sprites/player/ozonRed/rjl.png')]
                },
    'vel' : velo,
    'maxJumpHeight' : jump_height,
    'health' : health*1.2
}
players = {
    'blue'  : ozonBlue,
    'green' : ozonGreen,
    'red'   : ozonRed,
    'selected'     : [a for a in open(Path('Code/data/master.txt')).read().split(' ')][0],
    'attackUnlock' : [a for a in open(Path('Code/data/master.txt')).read().split(' ')][2]
    }

enemyMove = {
    'sprite' : {'walkRight' : [Path(r'Code/sprites/enemies/enemy1/monst_wr1.png'), Path(r'Code/sprites/enemies/enemy1/monst_wr2.png'), Path(r'Code/sprites/enemies/enemy1/monst_wr3.png'), Path(r'Code/sprites/enemies/enemy1/monst_wr4.png'), Path(r'Code/sprites/enemies/enemy1/monst_wr5.png')],
                'walkLeft' : [Path(r'Code/sprites/enemies/enemy1/monst_wl1.png'), Path(r'Code/sprites/enemies/enemy1/monst_wl2.png'), Path(r'Code/sprites/enemies/enemy1/monst_wl3.png'), Path(r'Code/sprites/enemies/enemy1/monst_wl4.png'), Path(r'Code/sprites/enemies/enemy1/monst_wl5.png')],
                'walkRightIce' : [Path(r'Code/sprites/enemies/enemy1/monst_ice_wr1.png'), Path(r'Code/sprites/enemies/enemy1/monst_ice_wr2.png'), Path(r'Code/sprites/enemies/enemy1/monst_ice_wr3.png'), Path(r'Code/sprites/enemies/enemy1/monst_ice_wr4.png'), Path(r'Code/sprites/enemies/enemy1/monst_ice_wr5.png')],
                'walkLeftIce' : [Path(r'Code/sprites/enemies/enemy1/monst_ice_wl1.png'), Path(r'Code/sprites/enemies/enemy1/monst_ice_wl2.png'), Path(r'Code/sprites/enemies/enemy1/monst_ice_wl3.png'), Path(r'Code/sprites/enemies/enemy1/monst_ice_wl4.png'), Path(r'Code/sprites/enemies/enemy1/monst_ice_wl5.png')],
                'walkRightFire' : [Path(r'Code/sprites/enemies/enemy1/monst_fire_wr1.png'), Path(r'Code/sprites/enemies/enemy1/monst_fire_wr2.png'), Path(r'Code/sprites/enemies/enemy1/monst_fire_wr3.png'), Path(r'Code/sprites/enemies/enemy1/monst_fire_wr4.png'), Path(r'Code/sprites/enemies/enemy1/monst_fire_wr5.png')],
                'walkLeftFire' : [Path(r'Code/sprites/enemies/enemy1/monst_fire_wl1.png'), Path(r'Code/sprites/enemies/enemy1/monst_fire_wl2.png'), Path(r'Code/sprites/enemies/enemy1/monst_fire_wl3.png'), Path(r'Code/sprites/enemies/enemy1/monst_fire_wl4.png'), Path(r'Code/sprites/enemies/enemy1/monst_fire_wl5.png')],
                },
    
    'vel' : velo*0.7,
    'maxJumpHeight' : jump_height,
    'health' : health * 0.3,
    'damage' : damage,
}
enemyStill = {
    'sprite' : {'walkRight' : [Path(r'Code/sprites/enemies/enemy2/monst_sr.png')],
                'walkLeft' : [Path(r'Code/sprites/enemies/enemy2/monst_sl.png')],
                'walkRightIce' : [Path(r'Code/sprites/enemies/enemy2/monst_ice_sr.png')],
                'walkLeftIce' : [Path(r'Code/sprites/enemies/enemy2/monst_ice_sl.png')],
                'walkRightFire' : [Path(r'Code/sprites/enemies/enemy2/monst_fire_sr.png')],
                'walkLeftFire' : [Path(r'Code/sprites/enemies/enemy2/monst_fire_sl.png')],
                },
    'vel' : velo*0,
    'maxJumpHeight' : 0,
    'health' : health * 0.9,
    'damage' : damage,
}

enemies = {
    'enemyMove' : enemyMove,
    'enemyStill' : enemyStill
}

# Maker Section
maker_sprites = {
    'side_bar'      :{
        'platforms' : {
            'grass' : Path(r'Code/sprites/levels/level1/ground.png'),
            'stone' : Path(r'Code/sprites/levels/level1/stone.png'),
            'poison': Path(r'Code/sprites/levels/level1/toxic.png'),
            'brown' : Path(r'Code/sprites/levels/level1/brown.png')
        },
        'enemies'   :{
            'walk1' : Path(r'Code/sprites/enemies/enemy1/monst_wr1.png'),
            'stand' : Path(r'Code/sprites/enemies/enemy2/monst_sr.png')
        },
        'berries'   :{
            'full'  : Path(r'Code/Assets/ozoBerry1.png'), 
            'part'  : Path(r'Code/Assets/ozoBerry2.png')
        },
        'bosses'    :{
            'b1'    :Path(r'Code/sprites/levels/level1/boss1.png'),
            'b2'    :Path(r'Code/sprites/levels/level2/boss2.png'),
            'b3'    :Path(r'Code/sprites/levels/level3/boss3.png'),
            'b4'    :Path(r'Code/sprites/levels/level4/boss4.png')
        }
    },
    'top_bar' : {
        'save'     : Path(r'Code/sprites/maker/save.png'),
        'platform' : Path(r'Code/sprites/maker/platforms.png'),
        'berry'    : Path(r'Code/sprites/maker/berries.png'),
        'enemy'    : Path(r'Code/sprites/maker/enemies.png'),  
        'boss'     : Path(r'Code/sprites/maker/boss.png'),  
    },
    'backgrounds' : {
        'night' : Path(r'Code/sprites/levels/level1/levelBack.png')
    }
}

start_sequence = {
    'imgs' : [Path(r'Code/Assets/startSequence1.png'),Path(r'Code/Assets/startSequence2.png'),Path(r'Code/Assets/startSequence3.png'),Path(r'Code/Assets/startSequence4.png'),Path(r'Code/Assets/startSequence5.png'),Path(r'Code/Assets/startSequence6.png'),Path(r'Code/Assets/startSequence7.png'),Path(r'Code/Assets/startSequence8.png'),Path(r'Code/Assets/startSequence9.png'),Path(r'Code/Assets/startSequence10.png')]
}
exit_sequence = {
    'imgs' : [Path(r'Code/Assets/EndingSequence1.png'),Path(r'Code/Assets/EndingSequence2.png'),Path(r'Code/Assets/EndingSequence3.png'),Path(r'Code/Assets/EndingSequence4.png')]
}

sequences = [start_sequence,exit_sequence]

fireBall = {
    'img' : Path(r'Code/Assets//Fireball.png'),
    'type' : 'fireBall',
    'velo' : 4,
    'damage': 10
}

iceBall = {
    'img' : Path(r'Code/Assets//iceball.png'),
    'type' : 'iceBall',
    'velo' : 3,
    'damage': 5
}

trashBall = {
    'img' : Path(r'Code/Assets//trashball.png'),
    'type' : 'trashBall',
    'velo' : 4,
    'damage': 10
}

normalBall = {
    'img' : Path(r'Code/Assets//normalBall.png'),
    'type' : 'normalBall',
    'velo' : 5,
    'damage' : 10
}

projectiles = {
    'fireBall' : fireBall,
    'iceBall' : iceBall,
    'trashBall': trashBall,
    'normalBall' : normalBall
}

home = {
    'default' : Path(r'Code/Assets/home.png'),
    'green': Path(r'Code/Assets/gl1.png'),
    'blue': Path(r'Code/Assets/gl2.png'),
    'red': Path(r'Code/Assets/gl3.png'),
}

# Bosses

b1 = {
    'projectile' : trashBall,
    'health' : health * 3,
    'damage' : damage*1.5,
    'size'   : boss_size,
    'sprite'  : { 
        'normal': Path(r'Code/sprites/levels/level1/boss1.png'),
        'ice': Path(r'Code/sprites/levels/level1/boss1Ice.png'),
        'fire': Path(r'Code/sprites/levels/level1/boss1Fire.png')
    }
                 
}
b2 = {
    'projectile' : trashBall,
    'health' : health * 3,
    'damage' : damage*1.5,
    'size'   : boss_size,
    'sprite'  : { 
        'normal': Path(r'Code/sprites/levels/level2/boss2.png'),
        'ice': Path(r'Code/sprites/levels/level2/boss2Ice.png'),
        'fire': Path(r'Code/sprites/levels/level2/boss2Fire.png')
    }
}
b3 = {
    'projectile' : trashBall,
    'health' : health * 3,
    'damage' : damage*1.5,
    'size'   : (boss_size[1],boss_size[1]),
    'sprite'  : { 
        'normal': Path(r'Code/sprites/levels/level3/boss3.png'),
        'ice': Path(r'Code/sprites/levels/level3/boss3Ice.png'),
        'fire': Path(r'Code/sprites/levels/level3/boss3Fire.png')
    }
}
b4 = {
    'projectile' : trashBall,
    'health' : health * 3,
    'damage' : damage*1.5,
    'size'   : (boss_size[1],boss_size[1]),
    'sprite'  : { 
        'normal': Path(r'Code/sprites/levels/level4/boss4.png'),
        'ice': Path(r'Code/sprites/levels/level4/boss4Ice.png'),
        'fire': Path(r'Code/sprites/levels/level4/boss4Fire.png')
    }
}

bosses = [b1,b2,b3,b4]