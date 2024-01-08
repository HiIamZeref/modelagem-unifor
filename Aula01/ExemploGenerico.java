import com.google.ortools.Loader;
import com.google.ortools.linearsolver.MPConstraint;
import com.google.ortools.linearsolver.MPObjective;
import com.google.ortools.linearsolver.MPSolver;
import com.google.ortools.linearsolver.MPVariable;

public class ExemploDinamico {
	
	public static void main(String[] args) {
		Loader.loadNativeLibraries();

		MPSolver solver = MPSolver.createSolver("SCIP");
		double infinity = java.lang.Double.POSITIVE_INFINITY;
		
		int n = 2;
		MPVariable[] x = new MPVariable[n];
		
		double[] c = {1, 10};
		double[][] A = {{1, 7}, {1, 0}};
		double[] b = {17.5, 3.5};

		for (int i = 0; i < n; i++) {
			x[i] = solver.makeIntVar(0.0, infinity, "x[" + (i+1) + ']');
		}
		System.out.println("Número de variáveis = " + solver.numVariables());
		
		for (int i = 0; i < A.length; i++) {
			MPConstraint cons = solver.makeConstraint(-infinity, b[i], "c" + i);
			for (int j = 0; j < n; j++) {
				cons.setCoefficient(x[j], A[i][j]);
			}
		}
		System.out.println("Número de restrições = " + solver.numConstraints());

		// Maximize x + 10 * y.
		MPObjective objective = solver.objective();
		for (int i = 0; i < c.length; i++) {
			objective.setCoefficient(x[i], c[i]);
		}
		objective.setMaximization();

		MPSolver.ResultStatus resultStatus = solver.solve();

		if (resultStatus == MPSolver.ResultStatus.OPTIMAL) {
			System.out.println("Solução:");
			System.out.println("Custo da função objetivo = " + objective.value());
			for (int i = 0; i < n; i++) {
				System.out.println(x[i].name() + " = " + x[i].solutionValue());
			}
			System.out.println("Tempo de resolução = " + solver.wallTime() + " milissegundos");
			System.out.println(solver.exportModelAsLpFormat());
		} else {
			System.out.println("Solução ótima não encontrada!");
		}

	}

}