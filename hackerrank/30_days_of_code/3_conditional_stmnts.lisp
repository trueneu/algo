(let ((n (parse-integer (read-line))))
     (let ((msg "Not Weird"))
          (cond ((or (oddp n) (and (<= n 20) (>= n 6))) (setq msg "Weird")))
          (format t "~a" msg)))
