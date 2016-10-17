(format t "The total meal cost is ~a dollars."
        (round
         (* (read-from-string (read-line))
            (+ 1 (/ (parse-integer (read-line)) 100)
               (/ (parse-integer (read-line)) 100)))))
