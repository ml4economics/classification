% GRADIENT DESCENT function.
% Iteratively optimizes theta model parameters.
function [theta, J, exit_flag] = gradient_descent(X, y, theta, lambda, options)
    % X - training set.
    % y - training output values.
    % theta - model parameters.
    % lambda - regularization parameter.
    % options - fminunc options
  
    % Optimize
    [theta, J, exit_flag] = fminunc(@(t)(gradient_callback(X, y, t, lambda)), theta, options);
end
