import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class CSVsearcher {
    private static List<String[]> data;

    public static void main(String[] args) {
        data = null;
        for (int i = 0; i < 3; i++) {
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
            System.out.print(".csvFilePath >");
            String file = null;
            try {
                file = reader.readLine();
                BufferedReader r = new BufferedReader(new FileReader(file));
                data = new ArrayList<>();
                String line;
                while ((line = r.readLine()) != null) {
                    String[] row = line.split(",");
                    data.add(row);
                }
                r.close();
                break;
            } catch (IOException e) {
                System.out.println("\u0007ERROR");
            }
        }

        if (data == null) {
            System.out.println("\u0007Limit exceeded.");
        }
        
        SwingUtilities.invokeLater(() -> createAndShowGUI());
    }

    private static boolean checkWordInText(String partialWord, String text) {
        Pattern pattern = Pattern.compile(Pattern.quote(partialWord), Pattern.CASE_INSENSITIVE);
        Matcher matcher = pattern.matcher(text);
        return matcher.find();
    }

    private static List<String[]> search(String word, List<String[]> data) {
        List<String[]> res = new ArrayList<>();
        if (!word.isEmpty()) {
            for (String[] row : data) {
                for (String cell : row) {
                    if (checkWordInText(word, cell)) {
                        res.add(row);
                        break;
                    }
                }
            }
        }
        return res;
    }

    private static void createAndShowGUI() {
        JFrame frame = new JFrame("蔵書検索");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel panel = new JPanel();
        panel.setLayout(new FlowLayout());

        final JLabel label = new JLabel();
        final JTextField textField = new JTextField(20);
        JButton searchButton = new JButton("検索");

        panel.add(label);
        panel.add(textField);
        panel.add(searchButton);

        final JTextArea textArea = new JTextArea(10, 40);

        searchButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String word = textField.getText();
                List<String[]> searchResult = search(word, data);
                StringBuilder resultText = new StringBuilder();
                int n = searchResult.size();
                for (String[] row : searchResult) {
                    for (String cell : row) {
                        resultText.append(cell).append(" / ");
                    }
                    resultText.append("\n\n");
                }
                textArea.setText(resultText.toString());
                label.setText(n + "件ヒット");
            }
        });

        JScrollPane scrollPane = new JScrollPane(textArea);

        frame.getContentPane().add(panel, BorderLayout.NORTH);
        frame.getContentPane().add(scrollPane, BorderLayout.CENTER);

        frame.pack();
        frame.setVisible(true);
    }
}
