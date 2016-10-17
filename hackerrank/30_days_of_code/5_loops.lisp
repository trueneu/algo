(let ((n (parse-integer (read-line))))
     (dotimes (i 10)
         (format t "~d x ~d = ~d~%" n (+ i 1) (* n (+ i 1)))))
