"""
    To Note:
            Loop Flow = [Initalize/Add ->(run): update, clear, draw]

    Finished:
    [X] - Add moving bullets to the player
    [X] - Fix bullet lifespan so they are not rendered after lifespan
    [X] - After bullets, fix handling of player "Hit" state. > hitstate should be temp then go back to idle
    [X] - Add a method for timing the death animation then freezing at end 
    [X] - Add another playerguy to test shooting for hit state and timer.
    [X] - Finally add health bar or similar and handle player death
    [X] - Limitation on bullets... Six shots then reload..("B" joystick button)    **Haven't added joystick yet**
    [X] - Sprite Manager for MainLoop to handle loader depending on player progress
    [X] - Remake/Organize main loop code for updating sprite classes, bg, drawing
    [X] - Camera
    [X] - UI for health, bullets/reloading
    [x] - moneybag class and bank?
    [x] - Dev mode for toggling hitbox rects, etc
    [X]- Y-Axis Perspective  
    [X] - Fix Game_Engine for proper game flow: (Add_Sprite, Run Loop > Update Sprites, Clear Screen, Events, Draw Sprites)
    [X] - Joystick loader 
    [X] - Cactus Enemy Class
    [X] - other obstacle classes? Buildings, Mailboxes & Fences, Trees/Tree_Stumps & Rocks, Wagons, etc ?
    [X] - Dev Mode for hitbox toggling outlines

    To Do:
    [] - Ammo_Box Class for tutorial?
    [] - (Enemy Classes: Coyote & Coffin) 
    [] - Cactus Hitbox/Collision Detection method during gameplay for player and obstacles
    [] - sound effects/music & hit/death screen effects = Gunshot, Reload, Hit, Dead. Background ole western soundtrack
    [] - Create town map
    [] - Level loader: (Init_Game, Tutorial state, Act I state, Act II state, Act III state, etc)
    [] - game storyline, etc (Save the Town?,whats the objective)
        [] - money buys bullets from the sheriff?
            |
            -> Thoughts:

                        1st state will be blocking off the town entrance until the tutorial is completed and the 
                        player is in possession of a pistol and bullets to go fight 

                        After the 1st bandit is defeated, then the entrance for the town becomes unlocked..

                        GameFlow: Tutorial, First BadGuy, Town, 
              
                [Intial state: Tutorial, then sheriff gives you task]

                        [Task one: Deal with bandits blocking road? -> after finish sheriff gives reward]
                        [Task two: Enter town, Deposit money at bank, encounter next bandits?]

*** Use a Json datasheet for a data_load method to load level data per level and gamestate ***

self.Levels = {
    "LevelOne": data_load(level_one),
}

            Data_Load(level) <- def method for loading level data
"""



"""

Levels = {
    "Level_One": 
}




"""

"""
Thoughts for the Town:
                        _______________________________________________________
                        [   sheriff                                 player    ]
                        [                                            pos      ]
                        [                                                     ]
                        [                                                     ]
                        [                                                     ]
                        [  tutorial                                  farm     ]
                        [______________________          _____________________]
                                               [        ]
                                               [        ]
                                               [        ]
                                               [         ]
                                               [          ]
                                               [           ]
                                               [            ]__________________      Town Entrance
                                               [                              ]          \  /
                                               [                              ]__         \/
                                               [                        1st   ] --> road blocked off until task
                                               [                                   complete & return to sheriff
                                               [                        task  ]___
                                               [______________________________]





"""