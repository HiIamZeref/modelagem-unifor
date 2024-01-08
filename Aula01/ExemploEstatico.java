
import com.google.ortools.Loader;
import com.google.ortools.linearsolver.MPConstraint;
import com.google.ortools.linearsolver.MPObjective;
import com.google.ortools.linearsolver.MPSolver;
import com.google.ortools.linearsolver.MPVariable;

public class ExemploEstatico {
	
	public static void main(String[] args) {
		Loader.loadNativeLibraries();

		MPSolver solver = MPSolver.createSolver("SCIP");
		double infinity = java.lang.Double.POSITIVE_INFINITY;

		// x1, x2 >= 0 e inteiros
		MPVariable x1 = solver.makeIntVar(0.0, infinity, "x1");
		MPVariable x2 = solver.makeIntVar(0.0, infinity, "x2");
		System.out.println("N�mero de vari�veis = " + solver.numVariables());

		// Maximize x1 + 10 * x2.
		MPObjective objective = solver.objective();
		objective.setCoefficient(x1, 1);
		objective.setCoefficient(x2, 10);
		objective.setMaximization();
		
		// x1 + 7 * x2 <= 17.5.
		MPConstraint c0 = solver.makeConstraint(-infinity, 17.5, "c0");
		c0.setCoefficient(x1, 1);
		c0.setCoefficient(x2, 7);

		// x1 <= 3.5.
		MPConstraint c1 = solver.makeConstraint(-infinity, 3.5, "c1");
		c1.setCoefficient(x1, 1);
		c1.setCoefficient(x2, 0);

		System.out.println("N�mero de restri��es = " + solver.numConstraints());

		

		MPSolver.ResultStatus resultStatus = solver.solve();

		if (resultStatus == MPSolver.ResultStatus.OPTIMAL) {
			System.out.println("Solu��o:");
			System.out.println("Custo da fun��o objetivo = " + objective.value());
			System.out.println("x1 = " + x1.solutionValue());
			System.out.println("x2 = " + x2.solutionValue());
			System.out.println("Tempo de resolu��o = " + solver.wallTime() + " milissegundos");
			System.out.println(solver.exportModelAsLpFormat());
		} else {
			System.out.println("Solu��o �tima n�o encontrada!");
		}

	}

}