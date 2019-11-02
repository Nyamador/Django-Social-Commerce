const path = require('path');
const webpack = require('webpack');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,
  entry: './static_src/index.js',
  output: {
      path: path.resolve(__dirname, 'static_build'),
      // path:  'static_build',
      filename: "[name]-[hash].js"
  },
  module:{
    rules: [
      { test: /\.js$/, exclude: /node_modules/, loader: "babel-loader" },
      {test: /\.css$/, use: ['style-loader', 'css-loader']},
    ],
  },

  // plugins: [
  //   new BundleTracker({filename: './webpack-stats.json'})
  // ],
  plugins: [
    new CleanWebpackPlugin(),
    new BundleTracker({filename: './webpack-stats.json'})
  ],

};
