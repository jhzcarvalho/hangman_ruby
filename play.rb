class Hangman

    def initialize
        @letters = ('a'..'z').to_a
        @word = words.sample
        @lives = 7
    end

    def words
        [
            ["cricket", "A game played by gentlemen"],
            ["jogging", "We are not walking..."],
            ["celebrate", "Remembering special moments"],
            ["continent", "There are 7 of these"],
            ["exotic", "Not from around here..."],
        ]
    end

    def print_teaser
        word_teaser = ""

        @word.first.size.times do
            word_teaser += "_ "
        end

        puts word_teaser
    end

    def make_guess
        if @lives > 0 
            puts "Enter a letter"
            guess = gets.chomp

            puts "You guessed #{guess}"

            # if letter is not part of word then remove from letters array
            good_guess = @word.first.include? guess
            
            if good_guess
                puts"Good guess"
                print_teaser
                
                make_guess
            else
                puts"Sorry... Try again!!"
                @lives -= 1  
                puts"You have #{@lives} left"  
                make_guess      
            end  
        else
            puts "Game Over"
        end 
    end 

    def begin
     # Asks user for a letter
        puts "New game started... your word is #{ @word.first.size} characters long"
        
        print_teaser
        puts "Your clue is #{ @word.last }"
        
        make_guess
    end
    
end

game = Hangman.new
game.begin