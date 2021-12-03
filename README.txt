        + ======================================================================================== +
        |                              [  Snake Class Methods  ]                                   |
        + ======================================================================================== +

    1)   snake_body()
            It Creates Initial snake body with Default position
            with Head and 3 Tail Segment

    2)   add_segment()
           +----------------------+---------------+
           | Parameter of Method  | Default Value |
           +----------------------+---------------+
           |     position         |  user_define  |
           |     shape            |  Square       |
           |     color            |  Black        |
           |     length           |  0.5          |
           |     width            |  0.5          |
           +----------------------+---------------+
           It Creates New Segment and Make Object of the Segment and,
           It Stores in snake_segment List

    3)  extend()
           It Creates New Segment at last and, at the position last segment
                (It helps to extend snake when snake eat food)

    4)  move()
           It Moves whole Snake Forward and, [ It Returns Position of Snake head ]

    5)  up()
           It Turns Head Up[ 90 ] degree

    6)  down()
           It Turns Head Down[ 270 ] degree

    7)  right()
           It Turns Head Right[ 0 ] degree

    8)  left()
           It Turns Head left[ 180 ] degree

    9)  reset()
           It Reset all values to default or Set all at stating point

    10) snake_boundary()
           +----------------------+---------------+
           | Parameter of Method  | Default Value |
           +----------------------+---------------+
           |     head_position    |  user_define  |
           |     x_positive       |  300          |
           |     x_negative       |  -300         |
           |     y_positive       |  300          |
           |     y_negative       |  -300         |
           +----------------------+---------------+
           It Set End Boundary of Snake at Position Snake can Move
           and , Return Boolean Value


  ========================================================================================================


        + ======================================================================================== +
        |                                [  Food Class Methods  ]                                  |
        + ======================================================================================== +

    1)  new_food()
           +----------------------+---------------+
           | Parameter of Method  | Default Value |
           +----------------------+---------------+
           |     x_pos_border     |  275          |
           |     x_neg_border     |  -275         |
           |     y_pos_border     |  275          |
           |     y_neg_border     |  -274         |
           +----------------------+---------------+
           It Creates Food with random location and,
           It Increases or Decreases area food show

    2)  is_food_eat()
           +----------------------+---------------+
           | Parameter of Method  | Default Value |
           +----------------------+---------------+
           |     snake_object     |  User_def     |
           +----------------------+---------------+
           Return Boolean value
           It checks Food is Eaten and,
           It Makes new food


  ========================================================================================================


        + ======================================================================================== +
        |                              [  Scoreboard Class Methods  ]                              |
        + ======================================================================================== +

    1)  scoreboard_body()
           +----------------------+--------------------------+
           | Parameter of Method  |      Default Value       |
           +----------------------+--------------------------+
           |     alignment        |  "center"                |
           |     font             |  ('Arial', 20, 'normal') |
           |     coordinate       |  None                    |
           +----------------------+--------------------------+
           It Creates scoreboard Body and,
           It set position Separately of ScoreBoard [IF needed]
           Note :- If you change position use [ scoreboard_coordinates ] Variable from class

             eg :- Import SnakeGame
                   scoreboard = SnakeGame.Scoreboard()
                   scoreboard.scoreboard_coordinates = (180, 270)
                        [Any Coordinates In Tuple(x, y)]

    2)  increase_score()
            It increases points by 1

    3)  reset()
            It Reset all values to default or Set score to [zero]
            Note:- It Not reset HighScore

    4)  game_over()
           +----------------------+--------------------------+
           | Parameter of Method  |      Default Value       |
           +----------------------+--------------------------+
           |     text             |  GAME OVER!              |
           |     alignment        |  "center"                |
           |     font             |  ('Arial', 20, 'normal') |
           +----------------------+--------------------------+
            It shows GAME OVER! Message at Middle of Screen
            IT changes Text                  |
            It changes Alignment of Message  |-- [If needed]
            IT changes Font of Message       |