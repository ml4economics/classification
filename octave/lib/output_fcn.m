% Output function to be passed to optimization algorithm fminunc

function stop = output_fcn(x, optimvalues, state)
  it = optimvalues.iter;
  if ( (it == 1) || (mod(it,10) == 0))
    fprintf("Iteration %d : %f\n", it, optimvalues.fval);
  endif
  stop = false;
end
