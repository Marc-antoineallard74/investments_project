import numpy as np
import matplotlib.pyplot as plt

def annualized_metrics(returns):
    mean_return = returns.mean() * 12
    std_dev = returns.std() * np.sqrt(12)
    sharpe_ratio = mean_return / std_dev
    return mean_return, std_dev, sharpe_ratio

# ----------------------------------- Plots ---------------------------------- #
def plot_decile_metrics(returns, title):
    # Calculate annualized mean, standard deviation, and Sharpe ratio
    metrics = returns.apply(annualized_metrics, axis=0)

    # As DataFrame
    metrics_df = metrics.T.rename(columns={0: 'Mean', 1: 'Volatility', 2: 'Sharpe Ratio'})

    # Plot
    metrics_df.plot(kind='bar', subplots=True, layout=(3, 1), figsize=(10, 8), title=title, legend=False)
    plt.tight_layout()
    plt.show()
    
def  plot_strategy_performance(data, metrics, columns):
    fig, axes = plt.subplots(1, len(metrics), figsize=(18, 6))


    for i, metric in enumerate(metrics):
        ax = axes[i]
        data.plot(kind='bar', x='Metric', y=[columns],
                    ax=ax, legend=True)
        ax.set_title(metric)
        ax.set_ylabel(metric)

    plt.tight_layout()
    plt.show()
